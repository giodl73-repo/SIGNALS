---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 14
rubric_version: v14
status: VARIATE
---

# mock-review Variate — Round 14

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v14 (C-01 through C-39; aspirational denominator = 31)
**Round:** R14 — targeting v14 new criteria: C-38, C-39

---

## What R13 Left Open

R13 (V-05 ceiling) achieved C-36 (independent Strategy-to-PM guard in Arch-first ordering),
C-37 (inherited from R13 baseline). All prior criteria preserved. Two residual gaps drive
C-38/C-39, derived from the same structural logic that produced C-32 over C-21 and C-34
over C-33:

| Criterion | R13 ceiling coverage | Gap |
|-----------|---------------------|-----|
| **C-37 → C-38** | R13 V-05 encodes the relationship between the MOCK-ACCEPTED rationale template and the REAL-REQUIRED decision template in surrounding guidance — describing symmetry in prose adjacent to the templates. The symmetry claim is advisory. | C-38 requires that cross-template relationships (symmetry, parallelism, contracts) are encoded as a named block at the template definition site — not descriptive prose in surrounding guidance. A CROSS-TEMPLATE RELATIONSHIP BLOCK must appear at the template site. A relationship stated in prose that a reader must cross-reference is not mechanically verifiable at the template site. |
| **C-38 structurally → C-39** | A structural block that co-locates the FORBIDDEN OUTPUTS TRIAD (satisfying C-27, C-29, C-31) carries no embedded explanation of *why* its co-location achieves independence from role ordering. The independence property is asserted but not declared. | C-39 requires that a structural block satisfying multiple criteria carries an embedded design note declaring which constraints it decouples and why. The TRIAD block satisfies C-27 (completeness), C-29 (co-location), C-31 (cardinality) — it must carry an embedded independence declaration naming which constraints it decouples from role sequence and the structural reason. |

- **C-38**: Template-site structural relationship block — cross-template relationships
  (symmetry, parallelism, verification contracts) encoded as a named block at the template
  definition site, not as descriptive prose in surrounding guidance
- **C-39**: Embedded structural independence declaration — a block satisfying multiple criteria
  carries an embedded design note declaring which constraints it decouples and why

Denominator: 29 → 31.

---

## Variation Axes and Hypotheses

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | Role sequence: Strategy→Architect→PM | Strategy-first surfaces tier-adequacy gaps before architectural analysis, blocking Architect analysis of tier-inadequate namespaces. Requires C-35 guard. C-36 does not apply. |
| V-02 | Output format: Table-centric decision blocks | Fixed-row tables enforce C-19 (structured trigger notation) mechanically; SQ answer vs verdict echo is distinguishable by row position rather than prose inspection. |
| V-03 | Inertia framing: Prominent DEFAULT DECISION POSITION block | Opening the skill with a named DEFAULT DECISION POSITION block makes burden-of-proof explicit before evaluation begins, forcing contrastive rationale rather than confirmatory rationale for every MOCK-ACCEPTED decision. |
| V-04 | Combined: Arch→Strat→PM + verbose lifecycle with step-name anchors | Canonical Arch-first ordering with verbose STOP gates and step-label anchors in every forward reference satisfies C-28 deeply and makes contamination paths self-identifying. |
| V-05 | Combined: Inertia + two-slot template + entity-naming SQs + C-38/C-39 | Decision inversion framing + Structural Position/Contrast two-slot template + entity-naming SQ grammar + C-38 cross-template block + C-39 independence declaration closes all remaining contamination paths. |

---

## V-01 — Role Sequence: Strategy→Architect→PM

**axis:** role-sequence
**hypothesis:** Strategy-first ordering fires the tier-coverage gate before architectural
analysis. Tier-inadequate namespaces are locked before Architect examines them, preventing
architecturally-plausible-but-tier-inappropriate namespaces from reaching PM. Requires C-35
(Strategy-to-PM guard). C-36 does not apply (not Arch-first). C-26 still fires (Arch before PM).
C-38/C-39 embedded in FORBIDDEN OUTPUTS TRIAD and MOCK-ACCEPTED template site.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
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

FORBIDDEN OUTPUTS TRIAD (3 rules, all required)
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (complete per-rule
  DO NOT set), C-29 (phase-gate co-location), and C-31 (cardinality header declaration)
  independently of role sequence. Its position at the phase gate decouples it from role
  ordering — the triad is verifiable in one scan here regardless of whether Strategy,
  Architect, or PM runs first. Role sequence affects Steps 3-5 only; this block is
  structurally upstream of all role steps. Changing role sequence does not move this
  block or alter its completeness guarantee. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] present.
  A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
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
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}").

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-35: non-Arch-first ordering guard):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. In this Strategy-first design, the
  Strategy-to-PM guard is the primary contamination control for PM evaluation. Applying
  PM to a Strategy-blocked namespace is the named error STRATEGY-GUARD-BYPASS.

Record before proceeding:
  Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
  Proceeding to Architect Evaluation: [{list}]

DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including Strategy-blocked — Architect still runs for
architecture coverage audit), answer sub-questions using entity-naming grammar.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the specific element").
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        (or: "Inconsistency found — name the specific element").
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names
  PM Evaluation (STEP 5) as the suppressed step. It is distinct from the Strategy-to-PM
  guard in STEP 3 — two independent guards, each firing on a distinct verdict value.

Record before proceeding:
  Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
  Proceeding to PM Evaluation: [{list}] (must be: remaining minus Strategy-blocked minus Arch-blocked)

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
  Position: second line of every REAL-REQUIRED block; "reason-code" line of MOCK-ACCEPTED.
  Values (canonical enumeration, equals-sign notation only):
    Auto:       trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation: trigger = STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED ↔ MOCK-ACCEPTED FIELD SYMMETRY
<!-- C-38: This named block encodes the cross-template structural relationship between
  the REAL-REQUIRED evaluation-driven decision template and the MOCK-ACCEPTED rationale
  template. The relationship is encoded here at the template definition site — not in
  surrounding prose. The symmetry must be verifiable at this block location without
  cross-referencing other sections. -->
| REAL-REQUIRED evaluation field         | MOCK-ACCEPTED structural analog         |
|----------------------------------------|----------------------------------------|
| trigger = {STRATEGY-INADEQUATE \|       | reason-code: [exact code from           |
|   ARCH-IMPLAUSIBLE \| PM-INCOMPLETE}   |   enumeration]                          |
| Failing verdict: {full verdict string} | Structural position: [SQ-1 anchor —     |
|                                        |   specific tier decision this feeds]    |
| SQ answer driving verdict: {artifact- | Contrast: [named namespace type +        |
|   state, artifact-as-subject form}     |   distinguishing structural factor]     |
| Artifact state: {present-tense,        | (Contrast slot corresponds to Artifact  |
|   artifact as subject}                 |   state: same constraint, opposite      |
|                                        |   direction — why threshold not crossed]|
| next-steps: /{skill} {topic} —         | next-steps: not generated (MOCK-        |
|   {Artifact state} [REQUIRED SLOT]     |   ACCEPTED namespaces do not appear)    |

A rationale that satisfies only one slot (Structural position or Contrast, not both)
is RATIONALE-INCOMPLETE — both slots are required.

SQ answer citation form: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: SQ answer with role as grammatical subject.
  Classification test: if the grammatical subject is a role name (Architect, PM, Strategy,
  or any evaluation noun), the field contains a VERDICT-ECHO — a named structural violation.
  "Section 4.1 contains no tier-boundary gate" = valid (artifact as subject).
  "Architect found no gate" = VERDICT-ECHO (role as subject — named error; rewrite required).
  This classification is deterministic from grammatical form alone. No content judgment needed.

MOCK-ACCEPTED template (requires all three role verdicts positive; PM-qualified only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes from this enumeration; no paraphrase; no invented codes)
  Structural position: Feeds tier decision: [SQ-1 answer — name the specific Tier {tier}
    decision this namespace supports. A generic adequacy statement without the SQ-1
    decision name = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast: [Name a namespace type that WOULD require real evidence AND the structural
    factor it has that this namespace lacks. Form: "Unlike {namespace type}, which carries
    {structural factor} requiring real evidence because {reason}, this namespace's outputs
    are fully determined by {structural form property}." A confirmatory sentence without
    a named contrasting namespace type = CONTRAST-INCOMPLETE.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. Observable state as predicate.]
    ERROR — VERDICT-ECHO [classification label]: grammatical subject is role name.
    Role-as-subject = VERDICT-ECHO (named violation, rewrite required).
    Artifact-as-subject = valid.
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
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
        Component-count rule: valid evaluation-driven entry has EXACTLY 3 components
          (skill-id, topic, Artifact state). A 2-component entry (skill-id + topic) is a
          TRACEABILITY-BREAK — classifiable at this template site from this definition alone.
        Tense/subject test: third component must be present-tense, artifact as subject.
          A third component with role as subject = VERDICT-ECHO-IN-NEXT-STEPS (distinct
          error class from TRACEABILITY-BREAK; also requires rewrite).
    Entry format (auto-flagged):
      /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical evaluation-driven REAL-REQUIRED (same entry formats)
  Priority 3 — Evidence-heavy and compliance REAL-REQUIRED:
    /{skill-id} {topic} — trigger: {EVIDENCE-HEAVY | COMPLIANCE}

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
  This is a canary: its presence asserts the condition. Writing it when the condition is
  not met is the named error CANARY-FALSE-POSITIVE — which destroys the assertion's value.
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"
  and complete remaining edits before re-verifying.

Full confirmation block (condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-02 — Output Format: Table-Centric Decision Blocks

**axis:** output-format
**hypothesis:** Structuring all decision blocks as fixed-row tables makes the trigger
field mechanically verifiable at a fixed row position (satisfying C-19 structurally), and
makes the SQ answer vs. verdict echo distinction observable by row label rather than
prose inspection. Tables also enforce two-slot MOCK-ACCEPTED rationale by making a missing
Contrast row visually apparent. Role sequence: canonical Arch→Strat→PM (C-26 + C-36 both
apply). C-38/C-39 embedded in FORBIDDEN OUTPUTS TRIAD block and decision table header.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
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

Output:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required)
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (enumerable per-rule
  DO NOT set), C-29 (co-located at phase gate), and C-31 (cardinality header declaration)
  independently of role sequence. The block's position at the phase gate is upstream of
  all role steps — its completeness guarantee is verifiable in one scan here regardless
  of role ordering. Moving role steps does not move this block. The independence property
  holds because co-location at the gate is a structural constraint on block position, not
  on evaluation sequence. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any evaluation outcome.
  All 3 labels must be present. 2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to auto-flagged namespaces. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Architect Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (table format; non-auto namespaces only)

For each remaining namespace, produce an Architect evaluation table:

| Field            | Value                                                                    |
|------------------|--------------------------------------------------------------------------|
| Namespace        | {name}                                                                   |
| SQ-1             | Name the component, dependency, or interface in the mock that confirms   |
|                  | plausibility — or "Contradiction: {named element}"                       |
| SQ-2             | Name the data flow, state transition, or API shape consistent with       |
|                  | {topic} architecture — or "Inconsistency: {named element}"               |
| SQ-3             | Name the architectural fact this namespace's mock most directly depends  |
|                  | on. State consistent or contradicts.                                     |
| architect-verdict| CONSISTENT-WITH-ARCHITECTURE  or  CONTRADICTS-ARCHITECTURE               |

CROSS-STEP GUARD — Architect to PM (C-26):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    DO NOT proceed to PM Evaluation (STEP 5) for this namespace.
    Named error for bypass: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy then PM: [{list}]

DO NOT proceed to STEP 4 (Strategy Evaluation) until all Architect tables and guard
assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (table format; non-auto namespaces only)

For each remaining namespace (including Arch-blocked for coverage synthesis), produce:

| Field             | Value                                                                   |
|-------------------|-------------------------------------------------------------------------|
| Namespace         | {name}                                                                  |
| SQ-1              | Name the specific Tier {tier} decision this namespace supports          |
| SQ-2              | Name the belief the team would form if this runs MOCK-ACCEPTED.         |
|                   | State: correct or incorrect.                                            |
| SQ-3              | Name the coverage gap keeping this namespace at REAL-REQUIRED default   |
|                   | — or "No gap: namespace positively demonstrates coverage adequacy"      |
| strategy-verdict  | ADEQUATE FOR TIER {tier}  or  INSUFFICIENT FOR TIER {tier}              |

CROSS-STEP GUARD — Strategy to PM (C-36: Arch-first design, independent of C-26):
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    DO NOT proceed to PM Evaluation (STEP 5) for this namespace.
    This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names
    PM Evaluation (STEP 5) as the suppressed step. It is structurally independent of
    the C-26 Architect-to-PM guard: C-26 fires on architect-verdict, this fires on
    strategy-verdict. Namespaces that pass Architect but fail Strategy are blocked here.
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

For each qualifying namespace:

| Field       | Value                                                                        |
|-------------|------------------------------------------------------------------------------|
| Namespace   | {name}                                                                       |
| SQ-1        | Name the required sections present in the mock artifact                      |
| SQ-2        | Name the enforcement gate, decision table, or required output structure      |
|             | present — or "Absent: {named missing element and defining section}"          |
| SQ-3        | Name one structural gap keeping this namespace at REAL-REQUIRED default      |
|             | — or "No gap: positively demonstrates structural completeness"               |
| pm-verdict  | STRUCTURALLY ADEQUATE  or  STRUCTURALLY INCOMPLETE                           |

DO NOT proceed to STEP 6 (Decision Tables) until all PM evaluation tables are complete.

---

STEP 6 — DECISION TABLES WITH CITATION

All decisions use a fixed-row table format. The `trigger` field appears at a fixed row
position in every table, making it mechanically parseable without prose interpretation.

CROSS-TEMPLATE RELATIONSHIP BLOCK — DECISION TABLE FIELD SYMMETRY
<!-- C-38: This named block encodes the structural relationship between the REAL-REQUIRED
  evaluation-driven decision table and the MOCK-ACCEPTED decision table. The relationship
  is a field-level symmetry: each row in the REAL-REQUIRED table has a corresponding
  structural analog in the MOCK-ACCEPTED table. This block is positioned at the template
  definition site — not in surrounding prose. The symmetry is verifiable at this block
  location without cross-referencing other sections. -->
| Row position | REAL-REQUIRED (eval) field    | MOCK-ACCEPTED field                   |
|--------------|-------------------------------|---------------------------------------|
| 1            | Decision: REAL-REQUIRED       | Decision: MOCK-ACCEPTED               |
| 2 (trigger)  | trigger = {rule label}        | trigger = n/a                         |
| 3            | Failing evaluation: {role}    | reason-code: [exact code]             |
| 4            | Failing verdict: {full string}| Structural position: [SQ-1 anchor]    |
| 5            | SQ answer driving verdict:    | Contrast: [named contrasting type +   |
|              |   {artifact-as-subject form}  |   structural factor]                  |
| 6            | Artifact state: {art-subj}    | (no analog — MOCK-ACCEPTED exits      |
| 7 (next-step)| /{skill} {topic} — {Art-st}   |   before next-steps generation)       |

Row 5 field grammar constraint (SQ answer):
  ERROR — VERDICT-ECHO [classification label]: grammatical subject is a role name.
  "Section 4.1 contains no tier-boundary gate" = valid (artifact-as-subject).
  "Architect found no gate" = VERDICT-ECHO (role-as-subject — named violation).
  In table format: the row label "SQ answer driving verdict:" guarantees structural
  separation from "Failing verdict:" — the error is detectable by row position.

MOCK-ACCEPTED decision table format:

| Field               | Value                                                              |
|---------------------|--------------------------------------------------------------------|
| Decision            | MOCK-ACCEPTED                                                      |
| trigger             | n/a                                                                |
| reason-code         | [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]    |
|                     | (exact codes; no paraphrase; both when applicable)                 |
| Structural position | Feeds tier decision: [SQ-1 answer — specific Tier {tier} decision |
|                     | this namespace supports. Generic adequacy = SLOT-VIOLATION.        |
|                     | Classify: STRUCTURAL-FORM or TIER-GATING]                          |
| Contrast            | Unlike {namespace type}, which carries {structural factor}         |
|                     | requiring real evidence because {reason}, this namespace's         |
|                     | outputs are fully determined by {structural form property}.        |
|                     | A confirmatory sentence without named contrasting namespace type   |
|                     | = CONTRAST-INCOMPLETE (named error; table row is required).        |

REAL-REQUIRED decision table format (evaluation-driven):

| Field                  | Value                                                         |
|------------------------|---------------------------------------------------------------|
| Decision               | REAL-REQUIRED                                                 |
| trigger                | {STRATEGY-INADEQUATE \| ARCH-IMPLAUSIBLE \| PM-INCOMPLETE}    |
| Failing evaluation     | [Strategy \| Architect \| PM]                                 |
| Failing verdict        | [full verdict string]                                         |
| SQ answer driving ver. | [present-tense, artifact-as-subject. Named error: VERDICT-    |
|                        | ECHO if role-as-subject — detectable by grammatical subject] |
| Artifact state         | [present-tense, artifact as subject]                          |

REAL-REQUIRED decision table format (auto-flagged):

| Field    | Value                                          |
|----------|------------------------------------------------|
| Decision | REAL-REQUIRED                                  |
| trigger  | {EVIDENCE-HEAVY \| TIER-CRITICAL \| COMPLIANCE} |

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
  ERROR — TRACEABILITY-BREAK [classification label]: evaluation-driven entry with 2
    components. Component-count rule: 3 required (skill-id, topic, Artifact state).
    2-component entries = TRACEABILITY-BREAK — classifiable at template site.
    Third-component form check: present-tense, artifact-as-subject. Role-as-subject
    in third component = VERDICT-ECHO-IN-NEXT-STEPS (distinct named error class).

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

## V-03 — Inertia Framing: Prominent DEFAULT DECISION POSITION Block

**axis:** inertia-framing
**hypothesis:** Opening the skill with a named DEFAULT DECISION POSITION block as the
primary structural element — before tier resolution, before auto-flagging, before any
template — makes REAL-REQUIRED inertia explicit and unignorable. Every phase refers back
to this block. The burden of proof is established structurally, not only in guidance.
MOCK-ACCEPTED becomes a named exception to a stated rule rather than a symmetric outcome.
Role sequence: Arch→Strat→PM (canonical). C-26 and C-36 both apply.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

===================================================================
DEFAULT DECISION POSITION (read this block before all other steps)
===================================================================

REAL-REQUIRED is the default decision for every namespace. This is not a starting guess —
it is the structural position from which every namespace must earn its way out.

MOCK-ACCEPTED is not a symmetric outcome. It is a named exception to the default that
requires the following conditions to be simultaneously true:
  1. The namespace is not auto-flagged by any automatic rule.
  2. All three role evaluations (Architect, Strategy, PM) return positive verdicts.
  3. A contrastive rationale is produced naming a contrasting namespace type that WOULD
     require real evidence, and the structural factor this namespace lacks.

A namespace that produces no contrastive argument remains REAL-REQUIRED. Absence of
disqualification is not positive evidence. Confirmation that nothing is wrong does not
earn escape from the default position.

This DEFAULT DECISION POSITION block establishes the inertia structure. Every phase below
refers to this structure. A namespace's path through the skill is: start at REAL-REQUIRED
→ attempt to earn MOCK-ACCEPTED → return to REAL-REQUIRED if the attempt fails at any step.

The default position is unconditional. No exceptional circumstances override it. No role
evaluation overrides it for auto-flagged namespaces.

===================================================================

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, current Status field from
each namespace section. Read TOPICS.md; record tier and compliance tags for {topic}.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three automatic rules. Mandatory. Not role-overridable. Auto-flagged namespaces are locked
at REAL-REQUIRED — the DEFAULT DECISION POSITION applies unconditionally; no argument
against the default is accepted for these namespaces.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: decision = REAL-REQUIRED, trigger = EVIDENCE-HEAVY
    (DEFAULT DECISION POSITION confirmed; no escape path available)

  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: decision = REAL-REQUIRED, trigger = TIER-CRITICAL
    (DEFAULT DECISION POSITION confirmed; tier criticality closes the escape path)

  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: decision = REAL-REQUIRED, trigger = COMPLIANCE
    (DEFAULT DECISION POSITION confirmed; compliance context closes the escape path)

Output:
  Locked at REAL-REQUIRED (auto): [{namespace}: trigger = {rule}]
  Attempting to earn MOCK-ACCEPTED (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required)
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (complete per-rule
  DO NOT set), C-29 (co-located at phase gate), and C-31 (cardinality header declaration)
  independently of role sequence. Its position upstream of all role steps means role
  ordering cannot affect this block's completeness. The DEFAULT DECISION POSITION block
  above establishes why these prohibitions exist structurally — auto-flagged namespaces
  have no escape path from REAL-REQUIRED, so marking them MOCK-ACCEPTED contradicts
  the inertia structure. This block encodes those prohibitions enumerably. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — confirms DEFAULT DECISION POSITION for auto namespaces):
  [EVIDENCE-HEAVY]  DO NOT mark EVIDENCE-HEAVY MOCK-ACCEPTED. These namespaces are locked.
  [TIER-CRITICAL]   DO NOT mark TIER-CRITICAL MOCK-ACCEPTED. These namespaces are locked.
  [COMPLIANCE]      DO NOT mark COMPLIANCE-tagged MOCK-ACCEPTED. These namespaces are locked.
  All 3 labels required. 2 of 3 = triad incomplete.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any locked namespace contradicts the DEFAULT DECISION POSITION.
  Named error: AUTO-RULE CONTAMINATION. Any verdict applied to a locked namespace is void.

Non-auto namespaces now begin their attempt to earn MOCK-ACCEPTED. They remain at
REAL-REQUIRED (DEFAULT DECISION POSITION) unless all three role evaluations positively
confirm eligibility. Each failed evaluation returns the namespace to REAL-REQUIRED.

DO NOT proceed to STEP 3 (Architect Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — ARCHITECT EVALUATION
(non-auto namespaces only — Attempt phase 1: architectural plausibility check)

Each namespace attempts to demonstrate architectural plausibility. Failure returns the
namespace to REAL-REQUIRED (DEFAULT DECISION POSITION).

Sub-questions (entity-naming grammar required):
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or "Contradiction: {specific named element}."
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or "Inconsistency: {specific named element}."
  SQ-3: Name the architectural fact about {topic} this namespace most depends on. State
        consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

Verdict CONTRADICTS-ARCHITECTURE returns namespace to REAL-REQUIRED (DEFAULT DECISION
POSITION confirmed). PM Evaluation does not run for returned namespaces.

CROSS-STEP GUARD — Architect to PM (C-26):
  IF architect-verdict = CONTRADICTS-ARCHITECTURE:
    decision = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed; attempt failed at Architect)
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Named bypass error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Returned to REAL-REQUIRED at Architect: [{list}]
    Continuing attempt — passed Architect: [{list}]

DO NOT proceed to STEP 4 (Strategy Evaluation) until all Architect verdicts and guard
assignments are complete.

---

STEP 4 — STRATEGY EVALUATION
(non-auto namespaces only — Attempt phase 2: coverage adequacy check)

Each namespace (including Architect-returned — Strategy runs for coverage synthesis)
attempts to demonstrate coverage adequacy for Tier {tier}. Failure returns the namespace
to REAL-REQUIRED (DEFAULT DECISION POSITION).

Sub-questions (entity-naming grammar required):
  SQ-1: Name the specific Tier {tier} decision this namespace supports.
  SQ-2: Name the belief the team would form about {topic} if this runs MOCK-ACCEPTED.
        State correct or incorrect.
  SQ-3: Name the coverage gap that would keep this namespace at its REAL-REQUIRED default
        — or "No gap: positively demonstrates coverage adequacy for Tier {tier}."

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

Verdict INSUFFICIENT FOR TIER {tier} returns namespace to REAL-REQUIRED (DEFAULT DECISION
POSITION confirmed). PM Evaluation does not run for returned namespaces.

CROSS-STEP GUARD — Strategy to PM (C-36: independent of Arch-to-PM guard):
  IF strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    decision = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed; attempt failed at Strategy)
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names
    PM Evaluation (STEP 5) as the suppressed step. It is independent of the C-26 guard:
    namespaces that pass Architect but fail Strategy are returned to default here.
    Named bypass error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Returned to REAL-REQUIRED at Strategy: [{list}]
    Continuing attempt — passed both Architect and Strategy: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until all Strategy verdicts and guard assignments
are complete.

---

STEP 5 — PM EVALUATION
(qualifying namespaces only — Attempt phase 3: structural completeness check)

Only namespaces that passed Architect and Strategy evaluations attempt PM. Failure here
returns the namespace to REAL-REQUIRED (DEFAULT DECISION POSITION). Applying PM to a
returned namespace is GUARD-BYPASS CONTAMINATION (named error).

Sub-questions (entity-naming grammar required):
  SQ-1: Name the required sections present in the mock artifact.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or "Absent: {named element} and {section defining it}."
  SQ-3: Name one structural gap that would keep this namespace at REAL-REQUIRED default
        — or "No gap: positively demonstrates structural completeness."

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

Verdict STRUCTURALLY INCOMPLETE returns namespace to REAL-REQUIRED (DEFAULT DECISION
POSITION confirmed). Only namespaces with STRUCTURALLY ADEQUATE here have earned MOCK-ACCEPTED
— pending the contrastive rationale required by the DEFAULT DECISION POSITION block.

DO NOT proceed to STEP 6 (Decisions) until all PM verdicts are complete.

---

STEP 6 — DECISIONS WITH CITATION

The DEFAULT DECISION POSITION block establishes the inertia structure for decision templates.

CROSS-TEMPLATE RELATIONSHIP BLOCK — DECISION FIELD CORRESPONDENCE
<!-- C-38: This named block encodes the cross-template structural relationship between the
  REAL-REQUIRED decision template and the MOCK-ACCEPTED rationale template at the template
  definition site. Both templates serve opposite sides of the same inertia structure:
  REAL-REQUIRED templates record the reason a namespace stays at default; MOCK-ACCEPTED
  templates record the argument that earned escape from default. The field correspondence
  must be verifiable here — not in prose adjacent to either template. -->

  The DEFAULT DECISION POSITION creates an asymmetric correspondence:
  REAL-REQUIRED fields record "why the attempt failed" → MOCK-ACCEPTED fields record "why the attempt succeeded"

  | Attempt-failed field (REAL-REQUIRED)  | Attempt-succeeded field (MOCK-ACCEPTED) |
  |---------------------------------------|----------------------------------------|
  | trigger = {rule or eval result}       | trigger = n/a (no rule fired)          |
  | Failing evaluation: {role}            | Structural position: {SQ-1 tier anchor}|
  | SQ answer driving verdict: {artifact} | (no analog — success has no "failing") |
  | Artifact state: {what failed}         | Contrast: {why threshold not crossed}  |
  | next-steps: /{skill} {topic} — {art.} | next-steps: not generated              |

  MOCK-ACCEPTED rationale MUST produce a genuine contrastive argument per DEFAULT DECISION
  POSITION. "Structural coverage is sufficient" is a confirmatory sentence, not a contrastive
  argument — it does not satisfy the Contrast slot. A contrastive argument names the specific
  structural factor that IS present in namespaces requiring real evidence and IS ABSENT here.

SQ answer citation grammar: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: role as grammatical subject.
  "Section 4.1 contains no tier-boundary gate" = valid.
  "Architect found no gate" = VERDICT-ECHO (role-as-subject; named violation; rewrite required).
  Classification test is deterministic from grammatical subject — no content judgment needed.

MOCK-ACCEPTED template:
  (Requires: auto-pass, all three role verdicts positive, contrastive rationale that satisfies
   both slots per DEFAULT DECISION POSITION inertia requirement)
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes; no paraphrase; no invented codes)
  Structural position: Feeds tier decision: [SQ-1 answer — specific Tier {tier} decision
    this namespace supports. Generic adequacy statement without SQ-1 citation = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast: [Name a namespace type that WOULD require real evidence AND the structural
    factor it has that this namespace lacks. Form: "Unlike {namespace type}, which carries
    {structural factor} requiring real evidence because {reason}, this namespace's outputs
    are fully determined by {structural form property}."
    Confirmatory sentence without named contrasting namespace type = CONTRAST-INCOMPLETE.
    A confirmatory sentence without this contrasting form violates the DEFAULT DECISION
    POSITION inertia requirement — it produces no argument against the default.]

REAL-REQUIRED template (evaluation-driven — namespace returned to default):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [present-tense, artifact-as-subject form]
    ERROR — VERDICT-ECHO [classification label]: role-as-subject = VERDICT-ECHO (named violation).
    Role-as-subject = VERDICT-ECHO. Artifact-as-subject = valid.
  Artifact state: [present-tense, artifact as subject — propagates to next-steps]

REAL-REQUIRED template (auto-flagged — namespace locked at default):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all namespace decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
Ordering rule (state in artifact): "Critical first ({trace-*, scout-feasibility, listen-*,
scout-competitors}), non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED (namespace locked or returned at Tier {tier}):
    /{skill-id} {topic} — {Artifact state}
    REQUIRED SLOT: {Artifact state} from STEP 6 decision block.
    ERROR — TRACEABILITY-BREAK [classification label]: 2-component entry.
      Component-count rule: 3 required. 2-component = TRACEABILITY-BREAK.
      Tense/subject check: third component present-tense, artifact-as-subject.
      Role-as-subject third component = VERDICT-ECHO-IN-NEXT-STEPS (distinct named error).
  Priority 2 — Non-critical evaluation-driven REAL-REQUIRED (same format)
  Priority 3 — Evidence-heavy and compliance (trigger propagation format):
    /{skill-id} {topic} — trigger: {EVIDENCE-HEAVY | COMPLIANCE}

  Cross-namespace risk statement (required):
    "Highest-risk gap: {namespace} — {Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 until review artifact confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory)

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH: Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (assertion): "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
PROHIBITED if any Status field remains. Named error: CANARY-FALSE-POSITIVE.
Suppression protocol: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — Combined: Arch→Strat→PM + Verbose Lifecycle with Step-Name Anchors

**axis:** canonical role sequence + verbose lifecycle emphasis
**hypothesis:** Arch-first ordering satisfies both C-26 (Arch-to-PM guard) and C-36
(independent Strategy-to-PM guard). Verbose STOP gates with step-label anchors in every
forward reference make contamination paths self-identifying — a reader who skips a gate
encounters the gate label explicitly named in the next blocked step. C-28 is deeply
satisfied: every forward reference carries both step number and step descriptive label.
C-38 and C-39 are embedded in both the TRIAD block and the MOCK-ACCEPTED template site.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED requires a positive argument
  against inertia. Confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ MOCK ARTIFACT AND TIER

Read {mock-artifact-path}. Extract namespace name, Category field, current Status field
from each namespace section. Read TOPICS.md; record tier and compliance tags for {topic}.

Output at the top of your response:
  "Tier: {N} (source: TOPICS.md | --tier | default)"

===== STEP 1 COMPLETE GATE =====
DO NOT proceed to Step 2 (Auto-Flag) until: namespace list is fully extracted with
Category and Status fields for every namespace. A partial extraction is not a valid
Step 1 completion. List all extracted namespaces before proceeding.
=================================

---

STEP 2 — AUTO-FLAG

Apply three mandatory rules. Rules fire unconditionally before role evaluation begins.
No role evaluation can override an automatic decision.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
    DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
    content depth, or any role evaluation outcome.

  RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
    DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. Tier criticality is structural.

  RULE 3 — COMPLIANCE (when compliance context is active):
    IF compliance tags present OR --compliance AND namespace in {scout-compliance,
      trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE
    DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED.

Output before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED, proceeding to evaluation): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required)
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (complete per-rule
  DO NOT set), C-29 (co-located at phase gate), and C-31 (cardinality header declaration)
  independently of role sequence. Co-location at the gate means the triad is verifiable
  in one scan before any role step runs. Arch-first ordering (Steps 3→4→5) places
  Architect before Strategy before PM. This block is independent of that ordering:
  the forbidden outputs apply to auto-flagged namespaces regardless of which role
  evaluation runs first. Decoupled constraints: (a) C-27 completeness from role step
  position; (b) C-31 cardinality from triad entry count; (c) C-29 co-location from
  role sequence. All three satisfied here without requiring a specific role ordering. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  All 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must be present.
  2 of 3 does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation (Architect, Strategy, PM) to any auto-flagged namespace.
  Named error: AUTO-RULE CONTAMINATION. Any verdict applied to an auto-flagged namespace
  is void and must be discarded.

===== PHASE GATE COMPLETE =====
DO NOT proceed to Step 3 (Architect Evaluation) until:
  (a) Two-list partition confirmed — every namespace in exactly one list.
  (b) FORBIDDEN OUTPUTS TRIAD verified complete — all 3 labels present.
  A phase gate with only 2 of 3 triad labels is not a valid gate completion.
================================

---

STEP 3 — ARCHITECT EVALUATION

For each remaining namespace, apply Architect evaluation. Sub-questions use entity-naming
grammar — "Name X" or "What specific X." A yes/no answer does not satisfy.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        architectural plausibility — or "Contradiction: {specific named element}."
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or "Inconsistency: {specific named element}."
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM Evaluation (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT proceed to Step 5 (PM Evaluation) for these namespaces.
    This guard fires on the specific verdict value `architect-verdict =
    CONTRADICTS-ARCHITECTURE` and names Step 5 (PM Evaluation) as the suppressed step.
    Named bypass error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Step 4 (Strategy Evaluation): [{list}]

===== STEP 3 COMPLETE GATE =====
DO NOT proceed to Step 4 (Strategy Evaluation) until: Architect verdict produced for
every remaining namespace AND Arch-blocked list and proceeding list are both recorded.
A Step 3 completion with a namespace missing an Architect verdict is not valid.
=================================

---

STEP 4 — STRATEGY EVALUATION

For each remaining namespace (including Arch-blocked — Strategy runs for all non-auto
namespaces for coverage synthesis), apply Strategy evaluation. Entity-naming grammar required.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED.
        State whether that belief would be correct or incorrect.
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or "No gap: namespace positively demonstrates coverage adequacy for Tier {tier}."

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM Evaluation (C-36: Arch-first design, independent of C-26):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT proceed to Step 5 (PM Evaluation) for these namespaces.
    This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names
    Step 5 (PM Evaluation) as the suppressed step. It is structurally independent of the
    C-26 guard in Step 3: C-26 fires on architect-verdict = CONTRADICTS-ARCHITECTURE;
    this guard fires on strategy-verdict = INSUFFICIENT FOR TIER {tier}. A namespace
    that passes Step 3 (Architect) but fails Step 4 (Strategy) is blocked by this guard,
    not C-26. The two guards together close both contamination vectors to PM:
    architecture-level (C-26) and coverage-adequacy-level (this guard, C-36).
    Named bypass error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Step 5 (PM Evaluation): [{list}]

===== STEP 4 COMPLETE GATE =====
DO NOT proceed to Step 5 (PM Evaluation) until: Strategy verdict produced for every
remaining namespace AND strategy-blocked list and proceeding list are both recorded.
A Step 4 completion with any namespace missing a Strategy verdict is not valid.
=================================

---

STEP 5 — PM EVALUATION

Entry condition: Step 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Applying PM to any blocked list namespace is GUARD-BYPASS
CONTAMINATION (named error) — the preliminary decision is already REAL-REQUIRED.

Sub-questions (entity-naming grammar — no yes/no answers):
  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or "Absent: {named missing element} and {section defining it}."
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or "No gap: namespace positively demonstrates structural completeness."

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

===== STEP 5 COMPLETE GATE =====
DO NOT proceed to Step 6 (Decisions with Citation) until: PM verdict produced for every
qualifying namespace (not on any blocked list). A Step 5 completion with a qualifying
namespace missing a PM verdict is not valid.
=================================

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named parseable artifact field at fixed position.
  Second line of every REAL-REQUIRED block (position = 2 from Decision).
  Values from canonical enumeration, equals-sign notation only:
    Auto-flagged: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: trigger = ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED ↔ MOCK-ACCEPTED STRUCTURAL SYMMETRY
<!-- C-38: This named block encodes the cross-template structural relationship between
  the REAL-REQUIRED evaluation-driven decision block and the MOCK-ACCEPTED rationale block
  at the template definition site. The symmetry is: every diagnostic field in the
  REAL-REQUIRED block (which records "why the attempt failed") has a structural analog
  in the MOCK-ACCEPTED block (which records "why the attempt succeeded"). This relationship
  cannot be verified from either template alone — it requires both templates to be
  compared. This block provides that comparison in one named location. -->
| REAL-REQUIRED diagnostic field      | MOCK-ACCEPTED structural analog                |
|-------------------------------------|------------------------------------------------|
| trigger = {rule label}              | trigger = n/a                                  |
| Failing evaluation: {role}          | — (no failing evaluation; all three passed)    |
| Failing verdict: {full string}      | reason-code: [exact reason code]               |
| SQ answer driving verdict: {art-    | Structural position: [SQ-1 answer as source    |
|   as-subj, present-tense}           |   — tier decision this namespace feeds]        |
| Artifact state: {art-as-subj}       | Contrast: [named contrasting type + factor]    |
| next-steps: /{sk} {tp} — {art-st}   | next-steps: not generated (no REAL-REQUIRED)   |

SQ answer citation grammar: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: role as grammatical subject.
  Role-as-subject = VERDICT-ECHO (named violation; rewrite required). Classifiable at
  field site — no cross-reference needed.
  "Section 4.1 contains no tier-boundary gate" = valid (artifact-as-subject).
  "Architect found no gate" = VERDICT-ECHO (role-as-subject).

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes; no paraphrase; no invented codes; both when applicable)
  Structural position: Feeds tier decision: [SQ-1 answer — name the Tier {tier} decision
    verbatim. Generic adequacy = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast: [Name a namespace type that WOULD require real evidence AND the structural
    factor it has that this namespace lacks. Form: "Unlike {namespace type}, which carries
    {structural factor} requiring real evidence because {reason}, this namespace's outputs
    are fully determined by {structural form property}."
    Confirmatory sentence only = CONTRAST-INCOMPLETE (named error). Both slots required.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE | PM-INCOMPLETE}
  Failing evaluation: [Architect | Strategy | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [present-tense, artifact-as-subject]
    ERROR — VERDICT-ECHO [classification label]: role-as-subject.
    Classification test: grammatical subject = role name → VERDICT-ECHO.
    Past-tense + role-as-subject = VERDICT-ECHO. Present-tense + artifact-as-subject = valid.
  Artifact state: [present-tense, artifact as subject]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

===== STEP 6 COMPLETE GATE =====
DO NOT proceed to Step 7 (Write Review Artifact) until: every namespace has a complete
decision block with all required fields populated. A namespace with any field missing
(including trigger or Artifact state) is not a valid Step 6 completion.
=================================

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
Header: Topic | Tier | Date
Coverage Review table: | Namespace | Category | Decision | trigger |

Ordering rule (state explicitly in artifact):
"Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
 non-critical evaluation-driven REAL-REQUIRED next, evidence-heavy and compliance last."

Priority 1 — Critical REAL-REQUIRED:
  Evaluation-driven entry format:
    /{skill-id} {topic} — {Artifact state}
    REQUIRED SLOT: `{Artifact state}` propagated from Step 6 decision block (field: Artifact state).
    ERROR — TRACEABILITY-BREAK [classification label]: entry with 2 components only.
      Component-count rule: valid evaluation-driven entry = 3 components (skill-id, topic,
        Artifact state). A 2-component entry = TRACEABILITY-BREAK — classifiable at this
        template definition site. No cross-referencing to REQUIRED SLOT declaration needed.
      Tense/subject test for third component: present-tense, artifact-as-subject.
        Role-as-subject in third component = VERDICT-ECHO-IN-NEXT-STEPS (named error class,
        distinct from TRACEABILITY-BREAK; equally void; requires rewrite).
  Auto-flagged entry format:
    /{skill-id} {topic} — trigger: {trigger value}

Priority 2 — Non-critical evaluation-driven REAL-REQUIRED (same entry formats)
Priority 3 — Evidence-heavy and compliance REAL-REQUIRED:
  /{skill-id} {topic} — trigger: {EVIDENCE-HEAVY | COMPLIANCE}

Cross-namespace risk statement (required output):
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

===== STEP 7 COMPLETE GATE =====
DO NOT proceed to Step 8 (Write Status Back) until: review artifact is confirmed written
with all four priority sections (use "(none)" for empty sections — do not omit) and
cross-namespace risk statement is present.
=================================

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using
Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH: Status: MOCK-ACCEPTED [reason-code] or Status: REAL-REQUIRED [trigger value]

Canary Confirmation:
  CANARY OUTPUT (assertion): "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error for false positive: CANARY-FALSE-POSITIVE (destroys the assertion's value).
  Suppression protocol: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
  Write canary only after verifying zero fields remain.

===== STEP 8 COMPLETE GATE — SKILL COMPLETE =====
Full confirmation block (write after canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
==================================================

---

## V-05 — Combined: Inertia + Two-Slot Template + Entity-Naming SQs + C-38/C-39

**axis:** inertia framing + two-slot MOCK-ACCEPTED template + entity-naming SQ grammar + C-38/C-39
**hypothesis:** The combination of (a) decision inversion framing with REAL-REQUIRED as
named default, (b) the Structural Position / Contrast two-slot MOCK-ACCEPTED rationale
template with dedicated labeled sub-slots, (c) entity-naming "Name X" grammar for all
sub-questions, (d) the C-38 cross-template relationship block at the MOCK-ACCEPTED template
site, and (e) the C-39 independence declaration embedded in the FORBIDDEN OUTPUTS TRIAD
block, closes all contamination paths identified in C-20, C-22, C-25, C-38, and C-39
simultaneously. A single-slot template allows confirmatory escape; the two-slot template
with a dedicated Contrast: row requires both structural position and contrastive argument.
C-38 makes the cross-template symmetry mechanically verifiable at the template site.
C-39 makes the TRIAD block's independence properties self-documenting.
Role sequence: Arch→Strat→PM (canonical). C-26 and C-36 both apply.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

===================================================================
DEFAULT DECISION POSITION
===================================================================

REAL-REQUIRED is the default. MOCK-ACCEPTED is not the default — it is an earned exception.

The inertia structure:
  — Every namespace starts at REAL-REQUIRED.
  — Automatic rules confirm REAL-REQUIRED unconditionally for auto-flagged namespaces.
    No argument earns escape for auto-flagged namespaces.
  — Role evaluation (Architect → Strategy → PM) tests whether a namespace can earn escape.
    Three sequential gates. Failure at any gate returns the namespace to REAL-REQUIRED.
  — MOCK-ACCEPTED requires passing all three gates AND producing a two-slot contrastive
    rationale. The Contrast slot requires a named contrasting namespace type + structural
    factor. A confirmatory argument does not earn escape.

This block is the authority for all decision logic below. References to "DEFAULT DECISION
POSITION" in subsequent steps refer here.

===================================================================

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category, current Status from each section.
Read TOPICS.md for tier and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. Mandatory. Not role-overridable. Fire before evaluation.

  RULE 1 — EVIDENCE-HEAVY: Category == EVIDENCE-HEAVY → REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL: tier >= 2 AND namespace in {trace-*, scout-feasibility,
    listen-*, scout-competitors} → REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE: compliance tags active AND namespace in {scout-compliance,
    trace-permissions} → REAL-REQUIRED, trigger = COMPLIANCE

Output:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required)
<!-- C-39 independence declaration: This block satisfies C-27 (complete per-rule DO NOT
  enumeration), C-29 (co-location at phase gate, upstream of all role steps), and C-31
  (cardinality header declaration) independently of each other and of role sequence.
  Constraint decoupling: (1) C-27 completeness is decoupled from role step position —
  the triad is verifiable in one scan here regardless of whether Architect, Strategy,
  or PM runs first; (2) C-31 cardinality is decoupled from triad entry content — the
  header "3 rules, all required" can be verified at the header level before reading
  entries; (3) C-29 co-location is decoupled from C-26 role ordering — placing the
  triad here satisfies both C-27 and C-29 without constraining which role runs first.
  The structural reason: a block positioned before all role steps is independent of
  role ordering by definition — its position is a phase-level constraint, not a role-
  sequence constraint. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — complete enumeration at this gate):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  All 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] required. 2 of 3 = gate incomplete.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Verdict applied to auto-flagged namespace = void (DEFAULT DECISION POSITION stands).

DO NOT proceed to STEP 3 (Architect Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

Entity-naming grammar required for all sub-questions. "Name X" and "What specific X" forms.
A yes/no answer does not satisfy entity-naming sub-question requirements.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        architectural plausibility for {topic} — or "Contradiction: {name the element}."
  SQ-2: Name the specific data flow, state transition, or API shape the mock implies
        — or "Inconsistency: {name the element}."
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. Name it and state: consistent or contradicts.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26):
  architect-verdict = CONTRADICTS-ARCHITECTURE:
    decision = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed at Architect gate)
    trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Named bypass error: ARCH-TO-PM-GUARD-BYPASS.
  Record: Arch-blocked [{list}] | Proceeding to Strategy [{list}]

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
assignments complete.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

Entity-naming grammar required. Arch-blocked namespaces also complete Strategy for coverage.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED.
        State whether that belief would be correct or incorrect.
  SQ-3: Name the coverage gap that would keep this namespace at its REAL-REQUIRED default
        — or "No gap: namespace positively demonstrates coverage adequacy for Tier {tier}."

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36: independent of C-26, Arch-first design):
  strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    decision = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed at Strategy gate)
    trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    This guard is structurally independent of C-26: it fires on a different verdict value
    (strategy-verdict vs architect-verdict) and covers the contamination path where a
    namespace passes Architect but fails Strategy. Without this independent guard, a
    Strategy-failed namespace would reach PM; this guard closes that vector.
    Named bypass error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record: Strategy-blocked [{list}] | Proceeding to PM [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments complete.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: only namespaces not on Arch-blocked or Strategy-blocked lists.
Applying PM to either blocked list = GUARD-BYPASS CONTAMINATION (named error).

Entity-naming grammar required.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure that is
        present — or "Absent: {name the missing element} — defined in {specific section}."
  SQ-3: Name one structural gap that would keep this namespace at its REAL-REQUIRED default
        — or "No gap: namespace positively demonstrates structural completeness."

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STRUCTURALLY INADEQUATE: decision = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed at PM gate)

DO NOT proceed to STEP 6 until PM verdicts complete for all qualifying namespaces.

---

STEP 6 — DECISIONS WITH CITATION

All three role verdicts positive = MOCK-ACCEPTED candidate. Rationale required.
Any verdict negative = REAL-REQUIRED (DEFAULT DECISION POSITION confirmed).

Trigger field: named, parseable, fixed-position field.
  Line 2 of every decision block. Equals-sign notation. Canonical values only:
    Auto: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation: ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE | PM-INCOMPLETE
  trigger = n/a for MOCK-ACCEPTED only.

SQ answer citation grammar: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [classification label]: role as grammatical subject.
  Classification test (at field site, no cross-reference needed):
    Subject = artifact name → valid citation.
    Subject = role name (Architect, Strategy, PM) → VERDICT-ECHO (named violation; void; rewrite).
  Structural signal: present-tense + artifact-subject distinguishes citation from
    past-tense + role-subject verdict echo. Both tense and subject are classifiable from
    the sentence alone. The error class is VERDICT-ECHO in both cases.

CROSS-TEMPLATE RELATIONSHIP BLOCK — MOCK-ACCEPTED ↔ REAL-REQUIRED FIELD SYMMETRY AND ASYMMETRY
<!-- C-38: This block encodes two cross-template relationships at the MOCK-ACCEPTED and
  REAL-REQUIRED template definition site: (1) field symmetry — every diagnostic field in
  the REAL-REQUIRED block has a structural analog in the MOCK-ACCEPTED block; (2) polarity
  asymmetry — the two templates carry opposite polarity for the DEFAULT DECISION POSITION:
  REAL-REQUIRED records failure to escape the default; MOCK-ACCEPTED records successful
  escape. Both relationships must be verifiable here without cross-referencing other sections.
  The block name "FIELD SYMMETRY AND ASYMMETRY" encodes both relationships in the block
  header — making the relationship type mechanically verifiable at the header level. -->

  Field symmetry (shared diagnostic role, opposite verdict):
  | Role               | REAL-REQUIRED field                  | MOCK-ACCEPTED field               |
  |--------------------|--------------------------------------|-----------------------------------|
  | Decision           | Decision: REAL-REQUIRED              | Decision: MOCK-ACCEPTED           |
  | Trigger/exit       | trigger = {rule label}               | trigger = n/a                     |
  | Verdict source     | Failing evaluation: {role}           | — (no failing evaluation)         |
  | Verdict value      | Failing verdict: {full string}       | reason-code: [exact code]         |
  | Diagnostic anchor  | SQ answer driving verdict: {art-    | Structural position: [SQ-1        |
  |                    |   as-subj, present-tense}            |   anchor — tier decision name]    |
  | State description  | Artifact state: {art-as-subj}        | Contrast: [named contrasting      |
  |                    |   (propagates to next-steps)         |   type + structural factor]       |

  Polarity asymmetry:
    REAL-REQUIRED template: populated when escape from DEFAULT DECISION POSITION failed.
    MOCK-ACCEPTED template: populated when escape succeeded AND contrastive rationale produced.
    Neither template produces the other's required fields — they are exclusive outputs.

MOCK-ACCEPTED template (two required slots — dedicated, labeled, mechanically separated):

  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    Exact codes from this enumeration. No paraphrase. No invented codes. Both when applicable.

  SLOT 1 — Structural position (Strategy SQ-1 anchor):
    Feeds tier decision: [Copy Strategy SQ-1 answer verbatim — name the specific Tier {tier}
      decision this namespace supports. This is a REQUIRED SLOT — generic adequacy
      without the SQ-1 decision name = SLOT-VIOLATION. The slot requires the SQ-1
      answer AND a type classification:]
    Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation needed)
           or TIER-GATING (tier-boundary decision requires real system-state evidence)
    [A generic adequacy statement ("this namespace has limited scope") without the SQ-1
      decision citation and classification = SLOT-VIOLATION. Both fields required.]

  SLOT 2 — Contrast (dedicated, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property} and do not depend on {what the contrasting factor produces at runtime}.
    [SLOT 2 is a dedicated, labeled sub-slot — not appended to Slot 1 and not optional.
      A rationale with only Slot 1 ("Structural position populated") and no separate Slot 2
      = RATIONALE-INCOMPLETE. The two-slot structure makes confirmatory escape impossible:
      Slot 1 states what tier decision this feeds (structural position); Slot 2 requires
      naming a contrasting namespace type that would need real evidence. A confirmatory
      sentence ("structural coverage is sufficient here") satisfies neither slot.
      Contrast slot validation: the sentence must name (a) a specific contrasting namespace
      type AND (b) a structural factor present in that type and absent in this namespace.
      Missing either (a) or (b) = CONTRAST-INCOMPLETE (named error, requires rewrite).]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE | PM-INCOMPLETE}
  Failing evaluation: [Architect | Strategy | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [present-tense, artifact as grammatical subject. Observable state as predicate.
      Name the specific artifact, section, or element whose state drove the verdict.]
    ERROR — VERDICT-ECHO [classification label]: grammatical subject is role name.
      Classification test (embedded, no cross-reference): if subject = role name → VERDICT-ECHO.
      "Section 4.1 contains no tier-boundary gate" = valid (artifact-as-subject, present-tense).
      "Architect found no gate" = VERDICT-ECHO (role-as-subject — named violation; rewrite).
      Past-tense with role-as-subject = VERDICT-ECHO regardless of content accuracy.
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until every namespace has a complete decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
Header: Topic | Tier | Date
Coverage Review table: | Namespace | Category | Decision | trigger |

Ordering rule (state explicitly in artifact):
"Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
 non-critical evaluation-driven REAL-REQUIRED next, evidence-heavy and compliance last."

Priority 1 — Critical REAL-REQUIRED:
  Evaluation-driven entry format:
    /{skill-id} {topic} — {Artifact state}
    REQUIRED SLOT: `{Artifact state}` propagated from STEP 6 (field: Artifact state).
    ERROR — TRACEABILITY-BREAK [classification label]: evaluation-driven entry with 2 components.
      Component-count rule: 3 required (skill-id, topic, Artifact state).
      A 2-component entry = TRACEABILITY-BREAK — classifiable at this template definition
        site from the component-count rule alone. No cross-reference to REQUIRED SLOT
        declaration needed. Present at the entry template definition site.
      Third-component form: present-tense, artifact-as-subject.
        Role-as-subject in third component = VERDICT-ECHO-IN-NEXT-STEPS (named error class,
        distinct from TRACEABILITY-BREAK; both require rewrite; both classifiable at entry site).
  Auto-flagged entry format:
    /{skill-id} {topic} — trigger: {trigger value}

Priority 2 — Non-critical evaluation-driven REAL-REQUIRED (same formats and error classes)
Priority 3 — Evidence-heavy and compliance:
  /{skill-id} {topic} — trigger: {EVIDENCE-HEAVY | COMPLIANCE}

Cross-namespace risk statement (required output):
  "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 until review artifact confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH: Status: MOCK-ACCEPTED [reason-code] or Status: REAL-REQUIRED [trigger value]

Canary Confirmation:
  CANARY OUTPUT: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This is a canary — its presence asserts the condition is met. Writing it when the
  condition is not met = CANARY-FALSE-POSITIVE (named error; destroys assertion value).
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Suppression: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
  Retry remaining edits. Re-verify. Write canary only when zero fields remain.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
