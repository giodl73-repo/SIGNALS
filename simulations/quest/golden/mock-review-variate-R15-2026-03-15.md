---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 15
rubric_version: v15
status: VARIATE
---

# mock-review Variate — Round 15

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v15 (C-01 through C-41; aspirational denominator = 33)
**Round:** R15 — targeting v15 new criteria: C-40, C-41

---

## What R14 Left Open

R14 achieved a 99.7 ceiling across all five variants, with a single missed aspirational point
in each variation: C-35 (unreachable in Arch-first designs) or C-36 (unreachable in Strat-first
designs). Two new criteria for R15 derive from the same structural escalation pattern that
produced C-32 over C-21 and C-38 over C-37:

| Criterion | R14 ceiling coverage | Gap |
|-----------|---------------------|-----|
| **C-39 structurally → C-40** | R14 V-05 named structural blocks satisfy multiple criteria, and the C-39 independence declaration names which criteria a block satisfies — but names them only in embedded HTML comments, not in the block headers themselves. The declaration is advisory metadata. | C-40 requires that named structural blocks carry criterion-ID parenthetical labels in their headers, declaring which criteria they satisfy at the block site. The label must appear in the block header, not in surrounding guidance or comments. A reviewer locates a named block and reads its header to confirm compliance — no rubric cross-referencing required. A block that carries correct content without a header label does not satisfy C-40; the label must be in the header itself. |
| **C-38 structurally → C-41** | R14 V-02 correspondence table rows carry field names and structural analogs. The symmetry is verifiable by scanning for field names. V-02's C-38 table uses a row-position column, but R14 V-01/V-03/V-04/V-05 encode correspondence via field-name inspection — row position is implicit. | C-41 requires row-position annotations in the CROSS-TEMPLATE RELATIONSHIP BLOCK correspondence table — each entry annotated with its row or field position alongside the field name (`Row 3: SQ answer driving verdict ↔ Row 3: Contrast`). The position annotation must appear in the table itself. A table that lists field names without positional anchors satisfies C-38 but not C-41; the position annotation must be a required column or inline label in the table definition. |

- **C-40**: Criterion-ID self-labeling in named structural blocks — every named structural block
  (guards, FORBIDDEN OUTPUTS TRIAD, CROSS-TEMPLATE RELATIONSHIP BLOCK, DEFAULT DECISION POSITION)
  carries a parenthetical criterion-ID label in its header, declaring which criterion(s) it
  satisfies at the block site. A block header without a criterion-ID parenthetical does not satisfy
  this criterion even if the block content is fully compliant.
- **C-41**: Row-position annotations in CROSS-TEMPLATE RELATIONSHIP BLOCK — the correspondence
  table annotates the row or field position for each entry alongside the field name, making
  the mapping mechanically verifiable by position. A table without position annotations satisfies
  C-38 but not C-41.

Denominator: 31 → 33.

---

## Variation Axes and Hypotheses

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | C-40 minimal scope + C-41 inline annotations, Strategy-first ordering | Applying criterion-ID labels to exactly the 4 named blocks in the C-40 definition (DEFAULT DECISION POSITION, guards, TRIAD, CROSS-TEMPLATE RELATIONSHIP BLOCK) satisfies C-40 without over-engineering. C-41 inline row-label annotations (`Row N: field`) satisfy the position-anchor requirement without a dedicated column. Strat-first: C-35 fires, C-36 N/A. |
| V-02 | C-41 dedicated row-number column, Arch-first, table-centric decision blocks | A dedicated leftmost `Row #` column in the correspondence table is mechanically cleaner than inline annotations: the row position is always in the first cell of each row, independent of column width. C-40 applied to 4 core blocks. Row position is readable before the field name. Arch-first: C-36 fires, C-35 N/A. |
| V-03 | C-40 maximum scope (all named structural elements), Arch-first | Extending criterion-ID labels beyond the 4 core blocks to every named gate, canary block, and next-steps template creates a fully self-referential skill where a reviewer can validate any criterion by label scan alone. C-41 inline. Arch-first. |
| V-04 | C-40 minimal + C-41 inline + Arch-first canonical + verbose step-name anchors | Minimal C-40 (4 core blocks) + inline C-41 + Arch-first ordering (C-26 + C-36 satisfied) + verbose step-name anchors in all forward references (deepening C-28 from R14 V-04) is the tightest combination: each structural decision is independently justified. |
| V-05 | C-40 maximum + C-41 dedicated column + polarity asymmetry + SQ propagation (combined ceiling) | Maximum C-40 scope + dedicated row-number column + R14 excellence signals (polarity asymmetry co-encoding, SQ forward-propagation annotation at collection site) produces the ceiling variation. Every structural claim is self-verifiable: criterion IDs label what each block satisfies, row numbers label where each field lives, polarity asymmetry makes the inertia structure verifiable from the template comparison alone. |

---

## V-01 — C-40 Minimal Scope + C-41 Inline, Strategy-first

**axis:** C-40-scope-minimal, C-41-inline
**hypothesis:** Criterion-ID labels on the 4 blocks named in C-40 definition satisfies C-40
completely. Inline row-label annotations (`Row N:`) in the correspondence table satisfy C-41
without a dedicated column. Strategy-first ordering (Strat→Arch→PM): C-35 fires, C-36 N/A.
All R14 V-01 patterns preserved; C-40 labels added to 4 core block headers; C-41 inline.

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
  independently of role sequence. Its position at the phase gate is upstream of all role
  steps — completeness verifiable in one scan here regardless of role ordering. Role
  sequence affects Steps 3-5 only; this block is structurally upstream of all of them. -->
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

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using "Name X" / "What specific X" grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}").

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-35, C-40):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. In this Strategy-first design, this is the
  primary contamination control for PM evaluation. Applying PM to a Strategy-blocked
  namespace is the named error STRATEGY-GUARD-BYPASS.

Record before proceeding:
  Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
  Proceeding to Architect Evaluation: [{list}]

DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including Strategy-blocked — Architect runs for coverage audit),
answer sub-questions using entity-naming grammar.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the specific element").
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        (or: "Inconsistency found — name the specific element").
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names
  PM Evaluation (STEP 5) as the suppressed step. It is distinct from the Strategy-to-PM
  guard in STEP 3 — two independent guards, each firing on a distinct verdict value.

Record before proceeding:
  Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
  Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and cross-step guard
assignments are complete.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Strategy-blocked or Arch-blocked
lists. Applying PM to either blocked list is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing and which section defines it").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: a named, parseable artifact field at fixed position in every decision block.
  Position: second line of every decision block; "reason-code" line of MOCK-ACCEPTED.
  Values (canonical enumeration, equals-sign notation only):
    Auto:       trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation: trigger = STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-41: Row-position annotations present in correspondence table — each entry labeled
  with Row N alongside field name, making correspondence verifiable by row position.
  C-40: This block header carries criterion-ID parenthetical (C-38, C-40, C-41). -->
| Row position | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|--------------|--------------------------------------------|------------------------------------------------------|
| Row 1        | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| Row 2        | trigger = {rule label}                     | trigger = n/a                                        |
| Row 3        | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| Row 4        | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor —                  |
|              |                                            |   specific tier decision this feeds]                 |
| Row 5        | SQ answer driving verdict:                 | Contrast: [named contrasting namespace type +        |
|              |   {present-tense, artifact-as-subject}     |   structural factor distinguishing it]               |
| Row 6        | Artifact state: {present-tense, art-subj}  | (no analog — MOCK-ACCEPTED exits before              |
| Row 7        | /{skill} {topic} — {Artifact state}        |   next-steps generation)                             |

Row-position verification: Row 2 carries trigger in BOTH templates. Row 5 carries the
SQ-diagnostic field in REAL-REQUIRED and the Contrast field in MOCK-ACCEPTED — the
structural analog of the diagnostic SQ answer is the contrastive argument.

SQ answer citation form: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: SQ answer with role as grammatical subject.
  "Section 4.1 contains no tier-boundary gate" = valid (artifact as subject).
  "Architect found no gate" = VERDICT-ECHO (role as subject — named violation; rewrite required).
  Classification is deterministic from grammatical subject alone.

MOCK-ACCEPTED template (requires all three role verdicts positive; PM-qualified only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes from this enumeration; no paraphrase; no invented codes)
  Structural position (SLOT 1 — Strategy SQ-1 anchor): Feeds tier decision: [SQ-1 answer —
    name the specific Tier {tier} decision this namespace supports. A generic adequacy
    statement without the SQ-1 decision name = SLOT-VIOLATION. Classify: STRUCTURAL-FORM
    | TIER-GATING.]
  Contrast (SLOT 2 — dedicated, structurally separate from Structural position):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. A confirmatory sentence without a named contrasting namespace type =
    CONTRAST-INCOMPLETE. A single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. Observable state as predicate.]
    ERROR — VERDICT-ECHO: grammatical subject is role name (named violation; rewrite required).
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision blocks.
DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in the artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED:
    Entry format (evaluation-driven):
      /{skill-id} {topic} — {Artifact state}
      REQUIRED SLOT: `{Artifact state}` propagates from the STEP 6 decision block.
      ERROR — TRACEABILITY-BREAK [classification label]: entry with 2 components only.
    Entry format (auto-flagged):
      /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical evaluation-driven REAL-REQUIRED
  Priority 3 — Evidence-heavy and compliance REAL-REQUIRED

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

Canary Confirmation:
  After completing all edits, verify before confirming.
  CANARY OUTPUT (assertion — write only when condition is verified true):
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

## V-02 — C-41 Dedicated Row Column, Arch-first, Table-Centric

**axis:** C-41-dedicated-column, output-format-table
**hypothesis:** A dedicated leftmost `Row #` column in the CROSS-TEMPLATE RELATIONSHIP
BLOCK is mechanically cleaner than inline row-label annotations: the row position is always
in the first cell, independent of column width or field name length. Readers locate any field
by scanning the row-number column first, then reading the field content. C-40 applied to 4
core named blocks. Role sequence: Arch→Strat→PM (C-26 + C-36 both fire). C-35 N/A.

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

Read {mock-artifact-path}. Extract namespace name, Category field, Status field from each
section. Read TOPICS.md for tier and compliance tags.

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
<!-- C-39 independence declaration: TRIAD satisfies C-27 (completeness), C-29 (co-location),
  C-31 (cardinality), C-39 (independence declaration), C-40 (header label) independently of
  role sequence. Phase-gate position is upstream of all role steps — the triad is verifiable
  in one scan here regardless of whether Architect, Strategy, or PM runs first. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  All 3 labels must be present. 2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to auto-flagged namespaces. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Architect Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (table format; non-auto namespaces only)

For each remaining namespace, produce an Architect evaluation table:

| Field             | Value                                                                     |
|-------------------|---------------------------------------------------------------------------|
| Namespace         | {name}                                                                    |
| SQ-1              | Name the component, dependency, or interface confirming plausibility —    |
|                   | or "Contradiction: {named element}"                                       |
| SQ-2              | Name the data flow, state transition, or API shape consistent with        |
|                   | {topic} architecture — or "Inconsistency: {named element}"                |
| SQ-3              | Name the architectural fact this namespace's mock most directly depends   |
|                   | on. State: consistent or contradicts.                                     |
| architect-verdict | CONSISTENT-WITH-ARCHITECTURE  or  CONTRADICTS-ARCHITECTURE                |

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    DO NOT proceed to PM Evaluation (STEP 5) for this namespace.
    Named error for bypass: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 (Strategy Evaluation) until all Architect tables and guard
assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (table format; non-auto namespaces only)

For each remaining namespace (including Arch-blocked — Strategy runs for coverage synthesis):

| Field             | Value                                                                     |
|-------------------|---------------------------------------------------------------------------|
| Namespace         | {name}                                                                    |
| SQ-1              | Name the specific Tier {tier} decision this namespace supports            |
|                   | [This answer populates the Structural position SQ-1 anchor — MOCK-       |
|                   | ACCEPTED template, Structural position slot.]                             |
| SQ-2              | Name the belief the team would form if this runs MOCK-ACCEPTED.           |
|                   | State: correct or incorrect.                                              |
| SQ-3              | Name the coverage gap keeping this namespace at REAL-REQUIRED default     |
|                   | — or "No gap: namespace positively demonstrates coverage adequacy"        |
| strategy-verdict  | ADEQUATE FOR TIER {tier}  or  INSUFFICIENT FOR TIER {tier}                |

CROSS-STEP GUARD — Strategy to PM (C-36, C-40): [Arch-first design, independent of C-26]
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    DO NOT proceed to PM Evaluation (STEP 5) for this namespace.
    C-36 fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM Evaluation
    (STEP 5) as the suppressed step. Structurally independent of C-26: fires on a different
    verdict value. Namespaces that pass Architect but fail Strategy are blocked here.
    Named error for bypass: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until all Strategy tables and guard assignments
are complete.

---

STEP 5 — PM EVALUATION (table format; qualifying namespaces only)

Entry condition: STEP 5 applies only to namespaces not on Arch-blocked or Strategy-blocked
lists. Applying PM to either blocked list = GUARD-BYPASS CONTAMINATION (named error).

| Field      | Value                                                                          |
|------------|--------------------------------------------------------------------------------|
| Namespace  | {name}                                                                         |
| SQ-1       | Name the required sections present in the mock artifact                        |
| SQ-2       | Name the enforcement gate, decision table, or required output structure        |
|            | present — or "Absent: {named missing element and defining section}"            |
| SQ-3       | Name one structural gap keeping this at REAL-REQUIRED default                  |
|            | — or "No gap: positively demonstrates structural completeness"                 |
| pm-verdict | STRUCTURALLY ADEQUATE  or  STRUCTURALLY INCOMPLETE                             |

DO NOT proceed to STEP 6 (Decision Tables) until all PM evaluation tables are complete.

---

STEP 6 — DECISION TABLES WITH CITATION

All decisions use fixed-row table format. Trigger field at fixed Row 2 position in every
decision table — mechanically parseable by row position without prose inspection.

CROSS-TEMPLATE RELATIONSHIP BLOCK — DECISION TABLE FIELD SYMMETRY (C-38, C-40, C-41):
<!-- C-38: Cross-template relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41: Dedicated leftmost Row # column — row position annotated as a required column
  alongside field name; correspondence verifiable by row number before reading field content.
  The dedicated column design is independent of field name length and column width. -->
| Row # | REAL-REQUIRED (eval) field                | MOCK-ACCEPTED structural analog                   |
|-------|-------------------------------------------|---------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                   | Decision: MOCK-ACCEPTED                           |
| 2     | trigger = {rule label}                    | trigger = n/a                                     |
| 3     | Failing evaluation: {role name}           | reason-code: [exact code from enumeration]        |
| 4     | Failing verdict: {full verdict string}    | Structural position: [SQ-1 anchor — tier decision |
|       |                                           |   this namespace feeds; SQ-1 answer required]     |
| 5     | SQ answer driving verdict:                | Contrast: [named contrasting namespace type +     |
|       |   {artifact-as-subject, present-tense}    |   structural factor distinguishing it]            |
| 6     | Artifact state: {art-subj, pres-tense}    | (no analog — MOCK-ACCEPTED exits before           |
| 7     | /{skill} {topic} — {Artifact state}       |   next-steps generation)                          |

Row 2 verification: trigger field appears at Row 2 in both templates.
  REAL-REQUIRED Row 2: trigger = {evaluation trigger value}
  MOCK-ACCEPTED Row 2: trigger = n/a
  Correspondence verifiable by row number alone.

Row 5 grammar constraint (SQ answer):
  ERROR — VERDICT-ECHO [classification label]: grammatical subject is a role name.
  "Section 4.1 contains no tier-boundary gate" = valid (Row 5, artifact-as-subject).
  "Architect found no gate" = VERDICT-ECHO (Row 5, role-as-subject — named violation).
  In dedicated-column format: Row 5 label guarantees structural separation from Row 4
  (Failing verdict) — echo is detectable by row number.

MOCK-ACCEPTED decision table format:

| Field                | Value                                                                      |
|----------------------|----------------------------------------------------------------------------|
| Decision (Row 1)     | MOCK-ACCEPTED                                                              |
| trigger (Row 2)      | n/a                                                                        |
| reason-code (Row 3)  | [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]            |
|                      | (exact codes; no paraphrase; no invented codes)                            |
| Structural position  | Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision |
| (Row 4 — SLOT 1,     | this namespace supports. Generic adequacy = SLOT-VIOLATION. Classify:      |
| Strategy SQ-1 anchor)| STRUCTURAL-FORM or TIER-GATING]                                            |
| Contrast (Row 5 —    | Unlike {namespace type}, which carries {structural factor} requiring real   |
| SLOT 2, dedicated)   | evidence because {reason}, this namespace's outputs are fully determined by |
|                      | {structural form property}. Missing named contrasting type = CONTRAST-      |
|                      | INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.                   |

REAL-REQUIRED decision table (evaluation-driven):

| Field                        | Value                                                              |
|------------------------------|--------------------------------------------------------------------|
| Decision (Row 1)             | REAL-REQUIRED                                                      |
| trigger (Row 2)              | {STRATEGY-INADEQUATE \| ARCH-IMPLAUSIBLE \| PM-INCOMPLETE}         |
| Failing evaluation (Row 3)   | [Strategy \| Architect \| PM]                                      |
| Failing verdict (Row 4)      | [full verdict string]                                              |
| SQ answer driving ver. (Row 5)| [present-tense, artifact-as-subject. Named error: VERDICT-ECHO   |
|                              | if role-as-subject — detectable at Row 5 by grammatical subject]  |
| Artifact state (Row 6)       | [present-tense, artifact as subject — propagates to next-steps]   |

REAL-REQUIRED decision table (auto-flagged):

| Field            | Value                                             |
|------------------|---------------------------------------------------|
| Decision (Row 1) | REAL-REQUIRED                                     |
| trigger (Row 2)  | {EVIDENCE-HEAVY \| TIER-CRITICAL \| COMPLIANCE}   |

Complete all namespace decision tables.
DO NOT proceed to STEP 7 until every namespace has a completed decision table.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
Ordering rule (state explicitly): "Critical first ({trace-*, scout-feasibility, listen-*,
scout-competitors}), non-critical evaluation-driven next, evidence-heavy and compliance last."

Next-steps entry format:
  Evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Auto-flagged: /{skill-id} {topic} — trigger: {trigger value}
  ERROR — TRACEABILITY-BREAK [classification label]: evaluation-driven entry with 2 components.
  3 components required (skill-id, topic, Artifact state). 2-component = TRACEABILITY-BREAK.

Cross-namespace risk statement (required):
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH: Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

Canary Confirmation:
  CANARY OUTPUT: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — C-40 Maximum Scope, Arch-first

**axis:** C-40-scope-maximum
**hypothesis:** Extending criterion-ID labels beyond the 4 core named blocks (guards, TRIAD,
CROSS-TEMPLATE RELATIONSHIP BLOCK, DEFAULT DECISION POSITION) to every named structural
element — role step completion gates, canary block, next-steps template, TRACEABILITY-BREAK
error block — creates a fully self-referential skill. A reviewer can validate compliance with
any criterion by scanning for its ID as a parenthetical label without consulting the rubric.
Role sequence: Arch→Strat→PM. C-36 fires, C-35 N/A. C-41 inline row annotations.

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
  Path through the skill: start at REAL-REQUIRED → attempt to earn MOCK-ACCEPTED → return
  to REAL-REQUIRED if the attempt fails at any gate.

---

STEP 1 — READ (C-08: tier resolution)

Read {mock-artifact-path}. Extract namespace name, Category field, Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output at top of response: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01: decision completeness, C-02: automatic rule correctness)

Apply all three rules before evaluation begins. Mandatory. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3, C-08):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present OR --compliance flag
    AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists (C-01: partition completeness):
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (complete per-rule
  DO NOT set), C-29 (phase-gate co-location), C-31 (cardinality header declaration),
  C-39 (independence declaration), and C-40 (criterion-ID header label) independently of
  role sequence. Completeness verifiable in one scan at this phase gate regardless of
  role ordering (Arch-first, Strat-first, or PM-first). Changing role sequence does not
  move this block or reduce its completeness guarantee. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. 2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

STEP 2 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 3 (Architect Evaluation) until:
  (a) Two-list partition confirmed — every namespace in exactly one list.
  (b) FORBIDDEN OUTPUTS TRIAD verified complete — all 3 labels present.

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13, C-40)

For each remaining namespace, answer sub-questions using entity-naming grammar.

  SQ-1 (C-15): Name the component, dependency, or interface in the mock confirming
        plausibility — or "Contradiction found: {named element}".
  SQ-2 (C-15): Name the data flow, state transition, or API shape the mock implies for
        {topic} — or "Inconsistency found: {named element}".
  SQ-3 (C-15): Name the architectural fact about {topic} this namespace most directly
        depends on. State: consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    DO NOT apply PM Evaluation (STEP 5) to this namespace.
    Named error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
  assignments complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-40)

For each remaining namespace (including Arch-blocked — Strategy runs for all):

  SQ-1 (C-15, C-23): Name the specific Tier {tier} decision this namespace supports.
        [This answer becomes the Structural position SQ-1 anchor in MOCK-ACCEPTED template.]
  SQ-2 (C-15): Name the belief the team would form if this runs MOCK-ACCEPTED.
        State whether that belief would be correct or incorrect.
  SQ-3 (C-15): Name the coverage gap keeping this namespace at REAL-REQUIRED default
        — or "No gap: namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40): [Arch-first design, independent of C-26]
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    DO NOT apply PM Evaluation (STEP 5) to this namespace.
    C-36 fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}`, names PM Evaluation
    (STEP 5) as suppressed step. Independent of C-26: fires on different verdict value.
    Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13, C-40)

Entry condition (C-17, C-26, C-36): STEP 5 applies ONLY to namespaces not on Arch-blocked
or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

  SQ-1 (C-15): Name the required sections present in the mock artifact.
  SQ-2 (C-15): Name the enforcement gate, decision table, or required output structure
        present — or "Absent: {named missing element and which section defines it}".
  SQ-3 (C-15): Name one structural gap keeping this namespace at REAL-REQUIRED default
        — or "No gap: positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts written for every
  qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30, C-40)

Trigger field: named, parseable field at fixed position.
  Position: second line of every decision block.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41):
<!-- C-38: Cross-template relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41: Inline row-position annotations — each field entry labeled Row N alongside field
  name. Position annotation is inline in the field cell, not a separate column. Row N
  annotation precedes the field name: "Row N: {field-name}: {content}". -->
| Row annotation               | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                     |
|------------------------------|--------------------------------------------|-----------------------------------------------------|
| Row 1: Decision              | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                             |
| Row 2: trigger               | trigger = {rule label}                     | trigger = n/a                                       |
| Row 3: Failing evaluation    | Failing evaluation: {role name}            | reason-code: [exact code]                           |
| Row 4: Failing verdict       | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor]                  |
| Row 5: SQ answer / Contrast  | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +             |
|                              |   {artifact-as-subject form}               |   structural factor]                                |
| Row 6: Artifact state        | Artifact state: {art-subj, pres-tense}     | (no analog)                                         |
| Row 7: Next-steps entry      | /{skill} {topic} — {Artifact state}        | (no analog)                                         |

Row 5 grammar constraint (C-21, C-32, C-40):
  SQ answer: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: role as grammatical subject at Row 5.
  Artifact-as-subject at Row 5 = valid; role-as-subject at Row 5 = VERDICT-ECHO.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30, C-40):
  Requires all three role verdicts positive; PM-qualified namespaces only.
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)
  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION. Classify:
    STRUCTURAL-FORM | TIER-GATING.]
  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence because
    {reason}, this namespace's outputs are fully determined by {structural form property}.
    Missing named contrasting namespace type = CONTRAST-INCOMPLETE.
    Single-slot rationale (Slot 1 only) = RATIONALE-INCOMPLETE.

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-24, C-40):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict (C-14, C-21):
    [Present-tense, artifact as subject. Observable state as predicate.
    ERROR — VERDICT-ECHO: grammatical subject is role name (named violation).]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps, C-24]

REAL-REQUIRED template — auto-flagged (C-02, C-06, C-40):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

STEP 6 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
  decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24, C-40)

Write simulations/mock/{topic}-review-{date}.md.
Ordering rule (C-05, C-40) — state explicitly in artifact:
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

Next-steps entry format (C-24, C-33, C-34, C-40):
  Evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Auto-flagged: /{skill-id} {topic} — trigger: {trigger value}
  ERROR — TRACEABILITY-BREAK [classification label]: 2-component evaluation-driven entry.
  3 components required. Role-as-subject in third component = VERDICT-ECHO-IN-NEXT-STEPS.

Cross-namespace risk statement (C-09, C-40):
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

STEP 7 COMPLETION GATE (C-18, C-28, C-40):
  DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (C-04, C-12, C-16, C-40): mandatory, non-skippable.

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY CONFIRMATION BLOCK (C-12, C-16, C-40):
  CANARY OUTPUT (assertion — write ONLY when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE — canary written when condition is not met.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — C-40 Minimal + C-41 Inline + Arch-first + Verbose Step-Name Anchors

**axis:** C-40-minimal, C-41-inline, lifecycle-emphasis
**hypothesis:** Minimal C-40 (4 core named blocks only) combined with C-41 inline row-label
annotations and verbose step-name anchors in every forward gate (deepening C-28 from R14 V-04)
produces the tightest combination: criterion-ID labeling covers exactly the blocks that satisfy
structural criteria, and every forward reference names both step number and step label, making
all gates self-resolving without external lookup. Role sequence: Arch→Strat→PM. C-35 N/A.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape. The inertia
  structure is unconditional: absence of disqualification does not earn escape. A genuine
  contrastive argument is required — naming a contrasting namespace type that WOULD require
  real evidence, and the structural factor this namespace lacks.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per section.
Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"

===== STEP 1 COMPLETE GATE =====
DO NOT proceed to Step 2 (Auto-Flag) until all namespace fields extracted and listed.
================================

---

STEP 2 — AUTO-FLAG

Three mandatory rules. Fire before evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY: IF Category == EVIDENCE-HEAVY THEN REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL:  IF tier >= 2 AND namespace in {trace-*, scout-feasibility,
                             listen-*, scout-competitors} THEN REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE:     IF compliance tags present AND namespace in {scout-compliance,
                             trace-permissions} THEN REAL-REQUIRED, trigger = COMPLIANCE

Output:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration: TRIAD satisfies C-27 (complete per-rule DO NOT set),
  C-29 (phase-gate co-location decoupled from role sequence), C-31 (cardinality header
  declaration), C-39 (independence declaration naming all three decouple pairs:
  (a) C-27 completeness decoupled from role step position,
  (b) C-31 cardinality decoupled from triad entry content,
  (c) C-29 co-location decoupled from C-26 role ordering),
  and C-40 (criterion-ID label in block header).
  Structural reason: a block positioned before all role steps is independent of role
  ordering by definition. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] present.
  2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

===== STEP 2 COMPLETE GATE =====
DO NOT proceed to Step 3 (Architect Evaluation) until:
  (a) Two-list partition confirmed — every namespace in exactly one list.
  (b) FORBIDDEN OUTPUTS TRIAD verified — all 3 labels present.
================================

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

Entity-naming SQ grammar required. Yes/no answers do not satisfy.

  SQ-1: Name the component, dependency, or interface in the mock confirming plausibility
        — or "Contradiction found: {named element}".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or "Inconsistency found: {named element}".
  SQ-3: Name the architectural fact about {topic} this namespace most directly depends on.
        State: consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (Step 5 — PM Evaluation) to this namespace.
    Named error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked: [{list}]
    Proceeding to Strategy Evaluation: [{list}]

===== STEP 3 COMPLETE GATE =====
DO NOT proceed to Step 4 (Strategy Evaluation) until Architect verdicts and guard
assignments complete for all remaining namespaces.
================================

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including Arch-blocked — Strategy runs for all):

  SQ-1: Name the specific Tier {tier} decision this namespace supports.
        [This answer propagates forward: it becomes the Structural position SQ-1 anchor
        in the MOCK-ACCEPTED template at Step 6 (Decisions with Citation).]
  SQ-2: Name the belief the team would form if this runs MOCK-ACCEPTED.
        State: correct or incorrect.
  SQ-3: Name the coverage gap keeping this at REAL-REQUIRED default — or "No gap: namespace
        positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40): [Arch-first design, independent of C-26]
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (Step 5 — PM Evaluation) to this namespace.
    C-36 fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}`.
    C-26 fires on `architect-verdict = CONTRADICTS-ARCHITECTURE`.
    The two guards close both contamination vectors to PM. Neither guard implies the other.
    Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}] (must be: remaining minus Arch-blocked minus Strategy-blocked)

===== STEP 4 COMPLETE GATE =====
DO NOT proceed to Step 5 (PM Evaluation) until Strategy verdicts and guard assignments
complete for all remaining namespaces.
================================

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on Arch-blocked or Strategy-blocked
lists. Named error: GUARD-BYPASS CONTAMINATION.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or "Absent: {named missing element and defining section}".
  SQ-3: Name one structural gap keeping this namespace at REAL-REQUIRED default
        — or "No gap: positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

===== STEP 5 COMPLETE GATE =====
DO NOT proceed to Step 6 (Decisions with Citation) until PM verdicts written for every
qualifying namespace.
================================

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named, parseable field at fixed second-line position in every decision block.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41):
<!-- C-38: Encoded at template definition site, not surrounding prose.
  C-40: Criterion-ID label in block header: (C-38, C-40, C-41).
  C-41: Inline row-position annotations — each row carries "Row N:" prefix in the
  left column, making correspondence verifiable by row number. Annotation is inline:
  the row position label appears as the left-column value alongside the field name. -->
| Row position          | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                   |
|-----------------------|--------------------------------------------|---------------------------------------------------|
| Row 1: Decision       | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                           |
| Row 2: trigger        | trigger = {rule label}                     | trigger = n/a                                     |
| Row 3: Failing eval   | Failing evaluation: {role name}            | reason-code: [exact code]                         |
| Row 4: Failing verd.  | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]|
| Row 5: SQ / Contrast  | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +           |
|                       |   {artifact-as-subject, present-tense}     |   structural factor]                              |
| Row 6: Artifact state | Artifact state: {art-subj, pres-tense}     | (no analog)                                       |
| Row 7: Next-steps     | /{skill} {topic} — {Artifact state}        | (no analog — MOCK-ACCEPTED exits)                 |

Row 2 carries trigger in both templates. Row 5 carries the SQ-diagnostic field (REAL-REQUIRED)
and the Contrast field (MOCK-ACCEPTED) — structural analogs at the same row position.
Row-position annotation makes both relationships verifiable by scanning the left column.

SQ answer grammar (Row 5): present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO: role name as grammatical subject at Row 5 (named violation).
  Row position makes the error classifiable without content inspection.

MOCK-ACCEPTED template (PM-qualified namespaces with all-positive role verdicts):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (SLOT 1 — Strategy SQ-1 anchor):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Missing named contrasting type = CONTRAST-INCOMPLETE.
    Single-slot rationale = RATIONALE-INCOMPLETE.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [artifact-as-subject, present-tense; ERROR — VERDICT-ECHO if role-as-subject]
  Artifact state: [present-tense, artifact as subject — propagates to Step 7 next-steps entry]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

===== STEP 6 COMPLETE GATE =====
DO NOT proceed to Step 7 (Write Review Artifact) until every namespace has a completed
decision block.
================================

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
Ordering rule (state explicitly): "Critical first ({trace-*, scout-feasibility, listen-*,
scout-competitors}), non-critical evaluation-driven next, evidence-heavy and compliance last."

Next-steps entry format:
  Evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Auto-flagged: /{skill-id} {topic} — trigger: {trigger value}
  ERROR — TRACEABILITY-BREAK: 2-component evaluation-driven entry (3 required).
  ERROR — VERDICT-ECHO-IN-NEXT-STEPS: role-as-subject in third component.

Cross-namespace risk statement:
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

===== STEP 7 COMPLETE GATE =====
DO NOT proceed to Step 8 (Write Status Back) until review artifact confirmed written.
================================

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place.
Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH: Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

Canary Confirmation:
  CANARY OUTPUT: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — C-40 Maximum + C-41 Dedicated Column + Polarity Asymmetry + SQ Propagation

**axis:** C-40-scope-maximum, C-41-dedicated-column, inertia-framing (combined ceiling)
**hypothesis:** Maximum C-40 (all named structural elements carry criterion-ID labels) +
dedicated row-number column for C-41 + R14 excellence signals (polarity asymmetry co-encoding
in cross-template block, SQ forward-propagation annotation at collection site) produces the
ceiling variation. Every structural claim is self-verifiable: criterion IDs label what each
block satisfies, row numbers label where each field lives, polarity asymmetry makes the
inertia structure verifiable from the template comparison alone without referencing the DEFAULT
DECISION POSITION block. Role sequence: Arch→Strat→PM. C-36 fires, C-35 N/A.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

===================================================================
DEFAULT DECISION POSITION (C-22, C-40) — read before all other steps
===================================================================

REAL-REQUIRED is the default decision for every namespace. This is not a starting guess —
it is the structural position from which every namespace must earn its way out.

MOCK-ACCEPTED is not a symmetric outcome. It is a named exception to the default that
requires three conditions simultaneously:
  1. The namespace is not auto-flagged by any automatic rule.
  2. All three role evaluations (Architect, Strategy, PM) return positive verdicts.
  3. A contrastive rationale is produced: a contrasting namespace type that WOULD require
     real evidence, and the structural factor this namespace lacks.

A namespace that produces no contrastive argument remains REAL-REQUIRED. Absence of
disqualification is not positive evidence. The default position is unconditional.

Path through the skill: start at REAL-REQUIRED → attempt to earn MOCK-ACCEPTED → return
to REAL-REQUIRED if the attempt fails at any gate. Only a successful escape at all gates
simultaneously produces MOCK-ACCEPTED.

===================================================================

---

STEP 1 — READ (C-01, C-08, C-40)

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per section.
Read TOPICS.md; record tier and compliance tags for {topic}.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"

===== STEP 1 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 2 (Auto-Flag) until all namespace fields extracted and listed.
====================================================

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-08, C-40)

Three mandatory rules. Fire before evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY: IF Category == EVIDENCE-HEAVY THEN REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL:  IF tier >= 2 AND namespace in {trace-*, scout-feasibility,
                             listen-*, scout-competitors} THEN REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE:     IF compliance tags present AND namespace in {scout-compliance,
                             trace-permissions} THEN REAL-REQUIRED, trigger = COMPLIANCE

Output partition:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration (systematic enumeration):
  (1) C-27 completeness is decoupled from role step position — the triad lists all three
      rules regardless of which role runs first; the completeness guarantee holds for any
      role sequence.
  (2) C-31 cardinality is decoupled from triad entry content — the header declares "3
      rules, all required" before enumerating entries; the cardinality claim is verifiable
      from the header alone.
  (3) C-29 co-location is decoupled from C-26 role ordering — the triad sits at the phase
      gate, upstream of all role steps; moving role steps does not move the triad block.
  Structural reason: a block positioned before all role steps is independent of role
  ordering by definition. Criterion-ID label in header satisfies C-40. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. 2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Applying evaluation to a locked namespace contradicts the DEFAULT DECISION POSITION.
  Any verdict applied to an auto-flagged namespace is void.

===== STEP 2 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 3 (Architect Evaluation) until:
  (a) Two-list partition confirmed — every namespace in exactly one list.
  (b) FORBIDDEN OUTPUTS TRIAD verified complete — all 3 labels present.
====================================================

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (C-07, C-13, C-15, C-40) (non-auto namespaces only)

Entity-naming SQ grammar required. Yes/no answers do not satisfy.

  SQ-1 (C-15): Name the component, dependency, or interface in the mock confirming
        plausibility — or "Contradiction found: {named element}".
  SQ-2 (C-15): Name the data flow, state transition, or API shape the mock implies for
        {topic} — or "Inconsistency found: {named element}".
  SQ-3 (C-15): Name the architectural fact about {topic} this namespace most directly
        depends on. State: consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (Step 5 — PM Evaluation) to this namespace.
    Named error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked: [{list}]
    Proceeding to Strategy Evaluation: [{list}]

===== STEP 3 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 4 (Strategy Evaluation) until Architect verdicts and guard
assignments complete for all remaining namespaces.
====================================================

---

STEP 4 — STRATEGY EVALUATION (C-07, C-13, C-15, C-23, C-40) (non-auto namespaces only)

For each remaining namespace (including Arch-blocked — Strategy runs for all):

  SQ-1 (C-15, C-23, C-30, C-40): Name the specific Tier {tier} decision this namespace
        supports. [This answer becomes the Structural position SQ-1 anchor in the MOCK-
        ACCEPTED template at Step 6 (Decisions with Citation) — SQ-1 is collected here
        and consumed at the Structural position slot. Author-side traceability: the answer
        you write here is required verbatim in the Structural position slot.]
  SQ-2 (C-15): Name the belief the team would form if this runs MOCK-ACCEPTED.
        State: correct or incorrect.
  SQ-3 (C-15): Name the coverage gap keeping this at REAL-REQUIRED default — or "No gap:
        namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40): [Arch-first design, independent of C-26]
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (Step 5 — PM Evaluation) to this namespace.
    C-36 fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}`.
    C-26 fires on `architect-verdict = CONTRADICTS-ARCHITECTURE`.
    Structurally independent: different verdict values, same target (PM Evaluation, Step 5).
    The two guards together close both contamination vectors to PM: a namespace that passes
    Architect but fails Strategy is blocked here; a namespace that fails Architect is blocked
    at Step 3. Without both guards independently, one contamination vector remains open.
    Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}]

===== STEP 4 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 5 (PM Evaluation) until Strategy verdicts and guard assignments
complete for all remaining namespaces.
====================================================

---

STEP 5 — PM EVALUATION (C-07, C-13, C-15, C-40) (qualifying namespaces only)

Entry condition (C-17, C-26, C-36): STEP 5 applies ONLY to namespaces not on Arch-blocked
or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

  SQ-1 (C-15): Name the required sections present in the mock artifact for this namespace.
  SQ-2 (C-15): Name the enforcement gate, decision table, or required output structure
        present — or "Absent: {named missing element and defining section}".
  SQ-3 (C-15): Name one structural gap keeping this namespace at REAL-REQUIRED default
        — or "No gap: positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

===== STEP 5 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 6 (Decisions with Citation) until PM verdicts written for every
qualifying namespace.
====================================================

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30, C-32, C-40)

Trigger field: named, parseable field at fixed second-line position.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — MOCK-ACCEPTED / REAL-REQUIRED FIELD SYMMETRY AND ASYMMETRY (C-38, C-40, C-41):
<!-- C-38: Encoded at template definition site. Both symmetry and polarity asymmetry encoded.
  C-40: Criterion-ID label in block header: (C-38, C-40, C-41).
  C-41: Dedicated Row # column — leftmost column, row position annotated as a required
  column alongside field names. Row position is always in the first cell, independent of
  field name length or column width. -->
FIELD SYMMETRY — each REAL-REQUIRED field has a MOCK-ACCEPTED structural analog:

| Row # | REAL-REQUIRED (eval) field                 | MOCK-ACCEPTED structural analog                       |
|-------|--------------------------------------------|-------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                               |
| 2     | trigger = {rule label}                     | trigger = n/a                                         |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]            |
| 4     | Failing verdict: {full verdict string}     | Structural position (SLOT 1): [SQ-1 anchor —          |
|       |                                            |   specific tier decision this feeds]                  |
| 5     | SQ answer driving verdict:                 | Contrast (SLOT 2): [named contrasting namespace type  |
|       |   {artifact-as-subject, present-tense}     |   + structural factor distinguishing it]              |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog)                                           |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog — MOCK-ACCEPTED exits)                     |

POLARITY ASYMMETRY — the templates carry opposite meanings relative to DEFAULT DECISION POSITION:
  REAL-REQUIRED (eval): records failure to escape the default. The namespace attempted to earn
    MOCK-ACCEPTED, and a role evaluation blocked it. The diagnostic fields (Row 3-5) record why
    the escape attempt failed.
  MOCK-ACCEPTED: records successful escape from the default. The namespace earned exception
    status at all three gates. The rationale fields (Row 3-5) record why the escape was earned.
  Neither template produces the other's required fields. They are exclusive outputs. The
  polarity asymmetry makes the inertia structure verifiable from this template comparison
  block alone — without referencing the DEFAULT DECISION POSITION block.

Row 2 verification: trigger field appears at Row 2 in both templates.
  REAL-REQUIRED Row 2: trigger = {evaluation trigger value} (records which rule or verdict blocked)
  MOCK-ACCEPTED Row 2: trigger = n/a (no blocking trigger — escape was earned)
  Asymmetry visible at Row 2: the trigger field encodes the escape attempt outcome in both templates.

Row 5 grammar constraint (C-21, C-32, C-40):
  SQ answer (REAL-REQUIRED Row 5): present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: role as subject at Row 5.
  "Section 4.1 contains no tier-boundary gate" = valid (artifact-as-subject, Row 5).
  "Architect found no gate" = VERDICT-ECHO (role-as-subject at Row 5 — named violation).
  Dedicated-column format: Row 5 label in Row # column guarantees structural separation
  from Row 4 — VERDICT-ECHO classifiable by row-number scan before reading content.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30, C-40):
  Requires all three role verdicts positive; PM-qualified namespaces only.
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes; no paraphrase; no invented codes — C-03)
  SLOT 1 — Structural position (Strategy SQ-1 anchor, C-23, C-30, C-40):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. SQ-1 answer collected at Step 4 SQ-1; written verbatim here. Generic adequacy
    statement without SQ-1 decision name = SLOT-VIOLATION. Classify: STRUCTURAL-FORM |
    TIER-GATING. The SQ-1 anchor makes Structural position verifiable against Step 4 output.]
  SLOT 2 — Contrast (dedicated, structurally separate from Slot 1, C-20, C-25, C-40):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}.
    CONTRAST-INCOMPLETE: sentence without a named contrasting namespace type.
    RATIONALE-INCOMPLETE: Slot 1 only (Slot 2 absent or empty).
    The two-slot structure is mechanical: a template with a single Rationale slot allows
    confirmatory sentences to satisfy the slot without a genuine contrastive argument.
    Two structurally separate slots require both components independently.

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-24, C-40):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict (C-14, C-21, C-32):
    [Present-tense, artifact as subject. Observable state as predicate.
    ERROR — VERDICT-ECHO [classification label]: grammatical subject is role name.
    Positive structural signal: "Section 4.1 contains no tier-boundary gate" (artifact-as-
    subject, present-tense, observable state). Named error distinguished from valid form by
    grammatical subject alone — no content judgment required.]
  Artifact state (C-24): [present-tense, artifact as subject — propagates to Step 7 next-steps]

REAL-REQUIRED template — auto-flagged (C-02, C-06, C-40):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

===== STEP 6 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 7 (Write Review Artifact) until every namespace has a completed
decision block.
====================================================

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24, C-40)

Write simulations/mock/{topic}-review-{date}.md.
Ordering rule (C-05) — state explicitly in artifact:
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

Next-steps entry format (C-24, C-33, C-34):
  Evaluation-driven: /{skill-id} {topic} — {Artifact state}
    REQUIRED: Artifact state propagates from Step 6 decision block (Row 6 field).
    ERROR — TRACEABILITY-BREAK [classification label]: 2-component evaluation-driven entry.
      3 components required (skill-id, topic, Artifact state). 2-component = TRACEABILITY-BREAK.
      Third-component tense/subject: artifact-as-subject, present-tense.
      ERROR — VERDICT-ECHO-IN-NEXT-STEPS: role-as-subject in third component (distinct error).
  Auto-flagged: /{skill-id} {topic} — trigger: {trigger value}

Cross-namespace risk statement (C-09):
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

===== STEP 7 COMPLETE GATE (C-18, C-28, C-40) =====
DO NOT proceed to Step 8 (Write Status Back) until review artifact confirmed written.
====================================================

---

STEP 8 — WRITE STATUS BACK (C-04, C-12, C-16, C-40): mandatory, non-skippable.

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY CONFIRMATION BLOCK (C-12, C-16, C-40):
  CANARY OUTPUT (assertion — write ONLY when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  Canary is a truth-encoding output: its presence asserts the condition is met; writing
  it when the condition is not met destroys the assertion's value — hence "false positive."
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
