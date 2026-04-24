---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-16
round: 6
rubric_version: v6
status: VARIATE
---

# mock-accept Variate — Round 6

**Date:** 2026-03-16
**Skill:** mock-accept
**Rubric:** v6 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-23 aspirational;
             C-22/C-23 new this round)
**Baseline:** R5 champion (V-05: full integration — SUBJECT-CHECK EXAMPLES TABLE +
             ENFORCEMENT NOTE with Violation: field + count-anchored assertion after
             CROSS-TEMPLATE RELATIONSHIP BLOCK + all R4 V-05 elements)
**Round:** R6 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R5 V-05 carries all C-17 through C-23 criteria. Under v6, C-22 and C-23 are newly codified.
R5 V-05 already satisfies both: C-22 via "Verify: all 7 field rows above are mapped before
filling either template" (count-anchored assertion), C-23 via the named `Violation:` field
inside the ENFORCEMENT NOTE block.

R6 targets three unexplored axes from the axis catalog: role sequence, inertia framing, and
numeric pre-decision scoring. These have not appeared in any prior round. Single-axis passes
V-01 through V-03 probe each axis in isolation. Combinations V-04 and V-05 test whether
role separation and inertia framing amplify argument quality, and whether the full triple
combination produces a new ceiling or introduces length-pressure degradation.

| Plan | Axis | Source criterion | What changes from R5 V-05 | Predicted |
|------|------|-----------------|--------------------------|-----------|
| V-01 | role-sequence | NEW: role-separation gate | Add explicit Coverage Analyst / Decision Authority split. After STEP 5, emit a role-separation GATE: "Analyst work complete. No decisions made. Observations only." STEP 6 relabeled as Decision Authority work. Decision Authority instruction: "Do NOT re-read {mock-artifact-path}." | Candidate C-24: role-separation gate check prevents early commitment bias; all other criteria unaffected |
| V-02 | inertia-framing | NEW: per-namespace inertia cost | Expand DEFAULT DECISION POSITION with a named cost-of-MOCK statement. Add `Cost-of-MOCK:` field to MOCK-ACCEPTED template and `Inertia validation:` field to REAL-REQUIRED template. Each decision names what tier decision stays unvalidated without real data. | Candidate C-25: per-namespace inertia cost named in decision block; amplifies MOCK-ACCEPTED Slot 1 specificity |
| V-03 | output-format | NEW: numeric pre-decision coverage score | Add `Score: {0-3}` after each role's SQ answers. Add COVERAGE SCORE TABLE after STEP 5. Binary verdict determined by score threshold (>=2 = adequate). | Candidate C-26: per-dimension coverage score forces explicit pre-verdict reasoning; discriminates partial coverage from no coverage |
| V-04 | role-sequence + inertia-framing | V-01 + V-02 combined | Coverage Analyst role produces per-namespace cost-of-MOCK observations. Decision Authority uses those observations plus named inertia costs to produce the final decision block. | C-24 and C-25 both pass; composite argument quality highest |
| V-05 | full integration | V-01 + V-02 + V-03 + R5 V-05 base | All three new axes plus all R5 elements. If C-24/C-25/C-26 all pass, score exceeds current ceiling and triggers rubric update. If length pressure degrades any criterion, V-05 identifies the binding constraint. | Golden candidate or rubric-update trigger |

---

## V-01 — Role Sequence: Coverage Analyst / Decision Authority Split

**axis:** role-sequence
**hypothesis:** R5 V-05 uses a single evaluator thread from STEP 1 through STEP 6 with no
structural break between observation and decision. A model that commits to a verdict during
evaluation (e.g., at SQ-2 in STEP 3) may write Slot 1 and Slot 2 as rationalization rather
than genuine coverage analysis. An explicit Coverage Analyst role (STEPS 1-5, observations
only, no decisions) with a role-separation gate before STEP 6 forces the Decision Authority
to work from a completed observation record rather than an in-progress evaluation. The gate
also creates a checkable structural property: if the Coverage Analyst emits any
MOCK-ACCEPTED / REAL-REQUIRED label before the gate, the gate fails with a named error.
Failure condition: if role separation does not change decision quality relative to R5 V-05,
the single-thread evaluation is already sufficient and structural gate adds no value.

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

===================================================================
COVERAGE ANALYST ROLE — STEPS 1 THROUGH 5
Role instruction: Produce observations only. No MOCK-ACCEPTED / REAL-REQUIRED decisions.
No decision labels of any kind may appear in Coverage Analyst output.
===================================================================

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: flag = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: flag = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: flag = COMPLIANCE

Output two lists:
  Auto-flagged: [{namespace}: flag = {rule}]
  Remaining: [{namespace}: Category = {value}]

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

Evaluation table format (auto-flagged rows receive SKIP in all evaluation columns):

| Namespace | Category | Auto-flag? | Arch SQ-1 | Arch SQ-2 | Arch SQ-3 | Arch Verdict |
|-----------|----------|-----------|-----------|-----------|-----------|--------------|
| {name} | {cat} | YES — SKIP | SKIP | SKIP | SKIP | SKIP |
| {name} | {cat} | no | {answer} | {answer} | {answer} | {verdict} |

  Sub-questions:
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or: "Inconsistency found — name the specific element".
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary observation = ARCH-IMPLAUSIBLE (no decision label yet — observation only)
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  bypass-error-code: ARCH-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Arch-blocked (CONTRADICTS-ARCHITECTURE):
      [{namespace list}]
      If empty: "Arch-blocked: [] (none — all remaining namespaces proceed to Strategy Evaluation)"
    Proceeding to Strategy Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to Strategy Evaluation: [] (none)"

DO NOT proceed to STEP 4 until Architect verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table from STEP 3, adding Strategy columns for qualifying rows:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [Becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary observation = STRATEGY-INADEQUATE (no decision label yet — observation only)
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}):
      [{namespace list}]
      If empty: "Strategy-blocked: [] (none — all remaining namespaces proceed to PM Evaluation)"
    Proceeding to PM Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to PM Evaluation: [] (none)"

DO NOT proceed to STEP 5 until Strategy verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table, adding PM columns for qualifying rows:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or: "Absent — name the missing element and which section defines it".
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 gate until PM verdicts are written for every qualifying namespace.

===================================================================
ROLE-SEPARATION GATE — COVERAGE ANALYST WORK COMPLETE
Gate check (required before Decision Authority begins):
  Confirm: Zero MOCK-ACCEPTED labels appear in Steps 1–5 output.
  Confirm: Zero REAL-REQUIRED labels appear in Steps 1–5 output.
  Observations are complete. Named error: ANALYST-PREMATURE-DECISION if either label found.
  "Coverage Analyst work complete: {N} namespaces observed, {N_auto} auto-flagged,
   {N_arch_blocked} arch-blocked, {N_strat_blocked} strategy-blocked,
   {N_qualifying} qualifying for PM evaluation."
===================================================================

===================================================================
DECISION AUTHORITY ROLE — STEP 6
Role instruction: Work from Coverage Analyst observations only.
DO NOT re-read {mock-artifact-path} in this role. Named error: AUTHORITY-REREAD.
===================================================================

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
| 4     | Failing verdict: {full verdict string}     | Contrast (SLOT 2 — write first):                     |
| 5     | SQ answer driving verdict (+ Error-code)   |   [Unlike {namespace type}...]                       |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Verify: all 7 field rows above are mapped before filling either template.
Count: 7 rows defined. Confirm 7 rows present before proceeding.

MOCK-ACCEPTED template (WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Claim: [write the SQ answer sentence here — present-tense]
    Subject-check: Identify the grammatical subject of your Claim sentence.
      If subject = role name (e.g., "Architect", "PM", "Strategy") → Error-code: VERDICT-ECHO
      If subject = artifact, section, or field (e.g., "Section 4.1", "The mock") → Error-code: NONE
    Error-code: [VERDICT-ECHO | NONE — based on Subject-check result above]
    SUBJECT-CHECK EXAMPLES TABLE:
      | Branch       | Claim form                                      | Error-code   |
      |--------------|------------------------------------------------|--------------|
      | VERDICT-ECHO | "Architect found no gate"                      | VERDICT-ECHO |
      | NONE         | "Section 4.1 contains no tier-boundary gate"   | NONE         |
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

CANARY TERMINOLOGY TABLE (read before branch definitions; do not skip):
  | Term                  | Type            | Meaning                                                |
  |-----------------------|-----------------|--------------------------------------------------------|
  | CANARY SUPPRESSED     | Correct output  | Edits incomplete; disclosure emitted; not an error     |
  | CANARY-FALSE-POSITIVE | Named error     | Assertion emitted when condition is false; wrong claim |

  ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-02 — Inertia Framing: Per-Namespace Cost-of-MOCK Statement

**axis:** inertia-framing
**hypothesis:** R5 V-05 frames inertia at the workflow level ("MOCK-ACCEPTED is an earned
escape requiring a positive argument against inertia") but does not require the decision
block itself to name what tier decision stays unvalidated if the namespace remains MOCK.
A decision-level inertia cost statement — `Cost-of-MOCK: [name the specific Tier {tier}
decision that proceeds without real validation if this namespace stays MOCK]` — anchors
MOCK-ACCEPTED decisions in comparative information value rather than abstract structural
adequacy. It also creates a directional constraint on REAL-REQUIRED: "Lift condition: [X]
would make MOCK structurally sufficient" names exactly what the team must do to validate
in a future round. This mirrors the inertia-framing pattern established for scout-feasibility
in R3, where anchoring RED blockers against status-quo workaround cost improved C-05 and
C-10 qualitative depth without changing rubric score.
Failure condition: if per-namespace cost statements produce boilerplate rather than specific
tier-decision names, the axis adds no discriminating signal over R5 V-05.

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

  COST-OF-MOCK FRAMING: Each namespace's mock coverage decision has a cost if wrong.
    MOCK-ACCEPTED (wrong): Team proceeds believing structural coverage is sufficient.
                           Real gap surfaces during integration. Cost: deferred rework.
    REAL-REQUIRED (wrong): Team blocks a namespace that could have proceeded as MOCK.
                           Cost: wasted real-data collection time.
  Name both costs explicitly per namespace in the decision block.

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

Evaluation table format (auto-flagged rows receive SKIP in all evaluation columns):

| Namespace | Category | Auto-flag? | Arch SQ-1 | Arch SQ-2 | Arch SQ-3 | Arch Verdict |
|-----------|----------|-----------|-----------|-----------|-----------|--------------|
| {name} | {cat} | YES — SKIP | SKIP | SKIP | SKIP | SKIP |
| {name} | {cat} | no | {answer} | {answer} | {answer} | {verdict} |

  Sub-questions:
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or: "Inconsistency found — name the specific element".
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  bypass-error-code: ARCH-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Arch-blocked (CONTRADICTS-ARCHITECTURE):
      [{namespace list}]
      If empty: "Arch-blocked: [] (none — all remaining namespaces proceed to Strategy Evaluation)"
    Proceeding to Strategy Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to Strategy Evaluation: [] (none)"

DO NOT proceed to STEP 4 until Architect verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table from STEP 3, adding Strategy columns for qualifying rows:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [Becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}):
      [{namespace list}]
      If empty: "Strategy-blocked: [] (none — all remaining namespaces proceed to PM Evaluation)"
    Proceeding to PM Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to PM Evaluation: [] (none)"

DO NOT proceed to STEP 5 until Strategy verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table, adding PM columns for qualifying rows:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or: "Absent — name the missing element and which section defines it".
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

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
| 4     | Failing verdict: {full verdict string}     | Contrast (SLOT 2 — write first):                     |
| 5     | SQ answer driving verdict (+ Error-code)   |   [Unlike {namespace type}...]                       |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Verify: all 7 field rows above are mapped before filling either template.
Count: 7 rows defined. Confirm 7 rows present before proceeding.

MOCK-ACCEPTED template (WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Cost-of-MOCK: [Name the specific Tier {tier} decision that proceeds without real-data
    validation if this namespace stays MOCK-ACCEPTED. Generic statement without named
    decision = COST-UNSPECIFIED. Error-code: COST-UNSPECIFIED if no tier decision named.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Claim: [write the SQ answer sentence here — present-tense]
    Subject-check: Identify the grammatical subject of your Claim sentence.
      If subject = role name (e.g., "Architect", "PM", "Strategy") → Error-code: VERDICT-ECHO
      If subject = artifact, section, or field (e.g., "Section 4.1", "The mock") → Error-code: NONE
    Error-code: [VERDICT-ECHO | NONE — based on Subject-check result above]
    SUBJECT-CHECK EXAMPLES TABLE:
      | Branch       | Claim form                                      | Error-code   |
      |--------------|------------------------------------------------|--------------|
      | VERDICT-ECHO | "Architect found no gate"                      | VERDICT-ECHO |
      | NONE         | "Section 4.1 contains no tier-boundary gate"   | NONE         |
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]
  Inertia validation: [Without real data for this namespace, the team proceeds without
    [name the specific unvalidated tier decision]. Lift condition: [name the exact structural
    change that would make MOCK sufficient for Tier {tier}.]
    Generic lift condition without named structural change = LIFT-UNSPECIFIED.]

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

CANARY TERMINOLOGY TABLE (read before branch definitions; do not skip):
  | Term                  | Type            | Meaning                                                |
  |-----------------------|-----------------|--------------------------------------------------------|
  | CANARY SUPPRESSED     | Correct output  | Edits incomplete; disclosure emitted; not an error     |
  | CANARY-FALSE-POSITIVE | Named error     | Assertion emitted when condition is false; wrong claim |

  ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-03 — Output Format: Numeric Pre-Decision Coverage Score (0-3)

**axis:** output-format
**hypothesis:** R5 V-05 uses binary verdicts at each evaluation step (CONSISTENT-WITH-
ARCHITECTURE / CONTRADICTS-ARCHITECTURE; ADEQUATE FOR TIER / INSUFFICIENT FOR TIER;
STRUCTURALLY ADEQUATE / STRUCTURALLY INCOMPLETE). A binary verdict compresses the
distinction between "barely adequate" (score 2) and "strongly covered" (score 3), and
between "minor gap" (score 1) and "structural impossibility" (score 0). Adding a numeric
Score: {0-3} field after each role's SQ answers — with score definitions anchored to
named structural evidence — forces explicit pre-verdict reasoning before the binary
decision fires. A COVERAGE SCORE TABLE after STEP 5 provides a single-view summary
of per-dimension scores before the decision authority enters STEP 6. This mirrors the
pre-decision scoring mechanism from scout-feasibility Tier scoring, where scoring each
component independently before the composite produces better composite calibration.
Failure condition: if per-dimension scores produce the same binary verdict every time
(all 0s or all 3s), the numeric scale adds no discriminating signal and the binary form
is already sufficient.

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

COVERAGE SCORE SCALE (used in STEPS 3, 4, 5):
  3 — Strong: named evidence present, no gap; structural property directly confirmed
  2 — Adequate: evidence present with minor gap; structural property inferred but defensible
  1 — Weak: evidence partial or indirect; gap present but not disqualifying
  0 — Absent: structural property unconfirmable from mock; gap is disqualifying
  Verdict threshold: Architect Score >= 2 = CONSISTENT-WITH-ARCHITECTURE
                     Strategy Score >= 2 = ADEQUATE FOR TIER {tier}
                     PM Score >= 2 = STRUCTURALLY ADEQUATE
  If score = 1 or 0: verdict = CONTRADICTS-ARCHITECTURE / INSUFFICIENT / INCOMPLETE respectively.
  Score must precede verdict. Named error: SCORE-AFTER-VERDICT if score field appears after verdict.

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

Evaluation table format (auto-flagged rows receive SKIP in all evaluation columns):

| Namespace | Category | Auto-flag? | Arch SQ-1 | Arch SQ-2 | Arch SQ-3 | Arch Score | Arch Verdict |
|-----------|----------|-----------|-----------|-----------|-----------|-----------|--------------|
| {name} | {cat} | YES — SKIP | SKIP | SKIP | SKIP | SKIP | SKIP |
| {name} | {cat} | no | {answer} | {answer} | {answer} | {0-3} | {verdict} |

  Sub-questions:
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or: "Inconsistency found — name the specific element".
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Arch Score: {0|1|2|3} — must appear before Arch Verdict. Named error: SCORE-AFTER-VERDICT.
  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE (Score >= 2)  or  CONTRADICTS-ARCHITECTURE (Score < 2)

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  bypass-error-code: ARCH-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Arch-blocked (CONTRADICTS-ARCHITECTURE):
      [{namespace list}]
      If empty: "Arch-blocked: [] (none — all remaining namespaces proceed to Strategy Evaluation)"
    Proceeding to Strategy Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to Strategy Evaluation: [] (none)"

DO NOT proceed to STEP 4 until Architect verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table from STEP 3, adding Strategy columns for qualifying rows:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [Becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Score: {0|1|2|3} — must appear before Strategy Verdict. Named error: SCORE-AFTER-VERDICT.
  Strategy Verdict: ADEQUATE FOR TIER {tier} (Score >= 2)  or  INSUFFICIENT FOR TIER {tier} (Score < 2)

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}):
      [{namespace list}]
      If empty: "Strategy-blocked: [] (none — all remaining namespaces proceed to PM Evaluation)"
    Proceeding to PM Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to PM Evaluation: [] (none)"

DO NOT proceed to STEP 5 until Strategy verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table, adding PM columns for qualifying rows:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or: "Absent — name the missing element and which section defines it".
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

  PM Score: {0|1|2|3} — must appear before PM Verdict. Named error: SCORE-AFTER-VERDICT.
  PM Verdict: STRUCTURALLY ADEQUATE (Score >= 2)  or  STRUCTURALLY INCOMPLETE (Score < 2)

DO NOT proceed to COVERAGE SCORE TABLE until PM verdicts are written for every qualifying namespace.

COVERAGE SCORE TABLE (emit before proceeding to STEP 6):
  | Namespace | Arch Score | Strategy Score | PM Score | Lowest Score | Preliminary |
  |-----------|-----------|---------------|---------|-------------|-------------|
  | {name}    | {0-3}     | {0-3}         | {0-3}   | {min}       | MA or RR    |
  Auto-flagged rows: omit from table (decisions are fixed by rule, not score).
  Arch-blocked rows: show Arch Score only; Strategy and PM = N/A.
  Strategy-blocked rows: show Arch + Strategy Score; PM = N/A.
  Preliminary: MA = MOCK-ACCEPTED candidate (all scores >= 2); RR = REAL-REQUIRED (any score < 2).

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
| 4     | Failing verdict: {full verdict string}     | Contrast (SLOT 2 — write first):                     |
| 5     | SQ answer driving verdict (+ Error-code)   |   [Unlike {namespace type}...]                       |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Verify: all 7 field rows above are mapped before filling either template.
Count: 7 rows defined. Confirm 7 rows present before proceeding.

MOCK-ACCEPTED template (WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  Failing score: [{0|1} — the score that caused the binary threshold to fail]
  SQ answer driving verdict:
    Claim: [write the SQ answer sentence here — present-tense]
    Subject-check: Identify the grammatical subject of your Claim sentence.
      If subject = role name (e.g., "Architect", "PM", "Strategy") → Error-code: VERDICT-ECHO
      If subject = artifact, section, or field (e.g., "Section 4.1", "The mock") → Error-code: NONE
    Error-code: [VERDICT-ECHO | NONE — based on Subject-check result above]
    SUBJECT-CHECK EXAMPLES TABLE:
      | Branch       | Claim form                                      | Error-code   |
      |--------------|------------------------------------------------|--------------|
      | VERDICT-ECHO | "Architect found no gate"                      | VERDICT-ECHO |
      | NONE         | "Section 4.1 contains no tier-boundary gate"   | NONE         |
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

CANARY TERMINOLOGY TABLE (read before branch definitions; do not skip):
  | Term                  | Type            | Meaning                                                |
  |-----------------------|-----------------|--------------------------------------------------------|
  | CANARY SUPPRESSED     | Correct output  | Edits incomplete; disclosure emitted; not an error     |
  | CANARY-FALSE-POSITIVE | Named error     | Assertion emitted when condition is false; wrong claim |

  ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-04 — Combined: Role Sequence + Inertia Framing

**axes:** role-sequence (V-01) + inertia-framing (V-02)
**hypothesis:** V-01 establishes that Coverage Analyst produces observations without decisions;
V-02 establishes that each decision names the cost of staying MOCK. Combining them: Coverage
Analyst observations include a per-namespace inertia note ("If this namespace stays MOCK:
[name the unvalidated tier decision]"), and Decision Authority uses those notes directly in
the Cost-of-MOCK field of the decision block. This creates a causal chain: observation names
the cost, decision confirms or challenges the cost, final block carries both. Predicted
excellence signal: MOCK-ACCEPTED Slot 1 specificity improves because the tier-decision anchor
(from V-02 inertia validation) is pre-established in Coverage Analyst output before Decision
Authority writes Slot 1. This may surface as a candidate C-24 (inertia cost pre-established in
observation before decision).
Failure condition: if the dual-role structure creates output length pressure that degrades
SUBJECT-CHECK EXAMPLES TABLE completeness (C-20), the combination is net-negative.

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

  COST-OF-MOCK FRAMING: Each namespace's mock coverage decision has a directional cost.
    MOCK-ACCEPTED (wrong): Team proceeds without real-data validation for a named tier decision.
    REAL-REQUIRED (wrong): Team blocks a namespace that could have proceeded as MOCK.
  Coverage Analyst records the inertia cost per namespace. Decision Authority uses it.

---

===================================================================
COVERAGE ANALYST ROLE — STEPS 1 THROUGH 5
Role instruction: Produce observations and inertia notes. No MOCK-ACCEPTED / REAL-REQUIRED
decision labels of any kind may appear in Coverage Analyst output.
===================================================================

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: flag = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: flag = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: flag = COMPLIANCE

Output two lists:
  Auto-flagged: [{namespace}: flag = {rule}]
  Remaining: [{namespace}: Category = {value}]

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

Evaluation table format (auto-flagged rows receive SKIP in all evaluation columns):

| Namespace | Category | Auto-flag? | Arch SQ-1 | Arch SQ-2 | Arch SQ-3 | Arch Verdict | Inertia Note |
|-----------|----------|-----------|-----------|-----------|-----------|--------------|-------------|
| {name} | {cat} | YES — SKIP | SKIP | SKIP | SKIP | SKIP | SKIP |
| {name} | {cat} | no | {answer} | {answer} | {answer} | {verdict} | {cost if MOCK} |

  Sub-questions:
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or: "Inconsistency found — name the specific element".
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE
  Inertia Note: Name the specific Tier {tier} decision that would proceed unvalidated if
    this namespace is eventually MOCK-ACCEPTED. Generic "tier decision" without naming
    the decision = INERTIA-UNSPECIFIED. This note propagates to the Decision Authority
    Cost-of-MOCK field.

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary observation = ARCH-IMPLAUSIBLE (no decision label — observation only)
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  bypass-error-code: ARCH-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Arch-blocked (CONTRADICTS-ARCHITECTURE):
      [{namespace list}]
      If empty: "Arch-blocked: [] (none — all remaining namespaces proceed to Strategy Evaluation)"
    Proceeding to Strategy Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to Strategy Evaluation: [] (none)"

DO NOT proceed to STEP 4 until Architect verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table from STEP 3, adding Strategy columns for qualifying rows:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [Becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary observation = STRATEGY-INADEQUATE (no decision label — observation only)
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}):
      [{namespace list}]
      If empty: "Strategy-blocked: [] (none — all remaining namespaces proceed to PM Evaluation)"
    Proceeding to PM Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to PM Evaluation: [] (none)"

DO NOT proceed to STEP 5 until Strategy verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table, adding PM columns for qualifying rows:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or: "Absent — name the missing element and which section defines it".
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 gate until PM verdicts are written for every qualifying namespace.

===================================================================
ROLE-SEPARATION GATE — COVERAGE ANALYST WORK COMPLETE
Gate check (required before Decision Authority begins):
  Confirm: Zero MOCK-ACCEPTED labels appear in Steps 1–5 output.
  Confirm: Zero REAL-REQUIRED labels appear in Steps 1–5 output.
  Confirm: Inertia Note is present for every non-auto-flagged namespace.
  Named error: ANALYST-PREMATURE-DECISION if any decision label found.
  Named error: INERTIA-NOTE-MISSING if any non-auto namespace lacks an Inertia Note.
  "Coverage Analyst work complete: {N} namespaces observed, {N_auto} auto-flagged,
   {N_arch_blocked} arch-blocked, {N_strat_blocked} strategy-blocked,
   {N_qualifying} qualifying for PM evaluation. Inertia Notes: {N_notes} recorded."
===================================================================

===================================================================
DECISION AUTHORITY ROLE — STEP 6
Role instruction: Work from Coverage Analyst observations and Inertia Notes only.
DO NOT re-read {mock-artifact-path} in this role. Named error: AUTHORITY-REREAD.
===================================================================

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
| 4     | Failing verdict: {full verdict string}     | Contrast (SLOT 2 — write first):                     |
| 5     | SQ answer driving verdict (+ Error-code)   |   [Unlike {namespace type}...]                       |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Verify: all 7 field rows above are mapped before filling either template.
Count: 7 rows defined. Confirm 7 rows present before proceeding.

MOCK-ACCEPTED template (WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Cost-of-MOCK: [From Coverage Analyst Inertia Note — name the specific Tier {tier} decision
    that proceeds without real-data validation if this namespace stays MOCK-ACCEPTED.
    If Inertia Note was INERTIA-UNSPECIFIED, this field must supply the named decision now.
    Generic statement without named decision = COST-UNSPECIFIED.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Claim: [write the SQ answer sentence here — present-tense]
    Subject-check: Identify the grammatical subject of your Claim sentence.
      If subject = role name (e.g., "Architect", "PM", "Strategy") → Error-code: VERDICT-ECHO
      If subject = artifact, section, or field (e.g., "Section 4.1", "The mock") → Error-code: NONE
    Error-code: [VERDICT-ECHO | NONE — based on Subject-check result above]
    SUBJECT-CHECK EXAMPLES TABLE:
      | Branch       | Claim form                                      | Error-code   |
      |--------------|------------------------------------------------|--------------|
      | VERDICT-ECHO | "Architect found no gate"                      | VERDICT-ECHO |
      | NONE         | "Section 4.1 contains no tier-boundary gate"   | NONE         |
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]
  Inertia validation: [Without real data for this namespace, the team proceeds without
    [name the specific unvalidated tier decision — from Inertia Note if present].
    Lift condition: [name the exact structural change that would make MOCK sufficient for Tier {tier}.]
    Generic lift condition without named structural change = LIFT-UNSPECIFIED.]

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

CANARY TERMINOLOGY TABLE (read before branch definitions; do not skip):
  | Term                  | Type            | Meaning                                                |
  |-----------------------|-----------------|--------------------------------------------------------|
  | CANARY SUPPRESSED     | Correct output  | Edits incomplete; disclosure emitted; not an error     |
  | CANARY-FALSE-POSITIVE | Named error     | Assertion emitted when condition is false; wrong claim |

  ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-05 — Full Integration: Role Sequence + Inertia Framing + Numeric Scoring

**axes:** role-sequence (V-01) + inertia-framing (V-02) + output-format / scoring (V-03)
         + all R5 V-05 base elements
**hypothesis:** All three R6 axes address independent structural locations:
  V-01 role-separation gate is between STEP 5 and STEP 6 (no structural overlap with V-02 or V-03)
  V-02 Cost-of-MOCK / Inertia validation fields are inside decision blocks (no overlap with V-01 gate)
  V-03 Score fields are inside evaluation tables and COVERAGE SCORE TABLE (no overlap with V-01 gate)
No two axes compete for the same structural slot. Predicted: all C-09 through C-23 criteria
carry from R5 V-05; C-24 (role-separation gate) and C-25 (per-namespace inertia cost named)
and C-26 (numeric pre-decision score) are probed simultaneously. If all three pass, this round
triggers three new aspirational criteria and raises the ceiling from 108.75 to a new maximum.
Failure condition: output length pressure from the combined triple-axis structure causes a
model to truncate or omit the SUBJECT-CHECK EXAMPLES TABLE (C-20) or COVERAGE SCORE TABLE
(V-03 addition). If truncation is observed, V-04 (dual-axis) is the ceiling form.

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

  COST-OF-MOCK FRAMING: Each namespace's mock coverage decision has a directional cost.
    MOCK-ACCEPTED (wrong): Team proceeds without real-data validation for a named tier decision.
    REAL-REQUIRED (wrong): Team blocks a namespace that could have proceeded as MOCK.
  Coverage Analyst records the inertia cost per namespace. Decision Authority uses it.

COVERAGE SCORE SCALE (used in STEPS 3, 4, 5):
  3 — Strong: named evidence present, no gap; structural property directly confirmed
  2 — Adequate: evidence present with minor gap; structural property inferred but defensible
  1 — Weak: evidence partial or indirect; gap present but not disqualifying
  0 — Absent: structural property unconfirmable from mock; gap is disqualifying
  Verdict threshold: Architect Score >= 2 = CONSISTENT-WITH-ARCHITECTURE
                     Strategy Score >= 2 = ADEQUATE FOR TIER {tier}
                     PM Score >= 2 = STRUCTURALLY ADEQUATE
  Score must precede verdict. Named error: SCORE-AFTER-VERDICT if score appears after verdict.

---

===================================================================
COVERAGE ANALYST ROLE — STEPS 1 THROUGH 5
Role instruction: Produce observations, scores, and inertia notes. No MOCK-ACCEPTED /
REAL-REQUIRED decision labels of any kind may appear in Coverage Analyst output.
===================================================================

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: flag = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: flag = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: flag = COMPLIANCE

Output two lists:
  Auto-flagged: [{namespace}: flag = {rule}]
  Remaining: [{namespace}: Category = {value}]

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

Evaluation table format (auto-flagged rows receive SKIP in all evaluation columns):

| Namespace | Category | Auto-flag? | Arch SQ-1 | Arch SQ-2 | Arch SQ-3 | Arch Score | Arch Verdict | Inertia Note |
|-----------|----------|-----------|-----------|-----------|-----------|-----------|--------------|-------------|
| {name} | {cat} | YES — SKIP | SKIP | SKIP | SKIP | SKIP | SKIP | SKIP |
| {name} | {cat} | no | {answer} | {answer} | {answer} | {0-3} | {verdict} | {cost if MOCK} |

  Sub-questions:
  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2: Name the data flow, state transition, or API shape the mock implies for {topic}
        — or: "Inconsistency found — name the specific element".
  SQ-3: Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Arch Score: {0|1|2|3} — must appear before Arch Verdict. Named error: SCORE-AFTER-VERDICT.
  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE (Score >= 2)  or  CONTRADICTS-ARCHITECTURE (Score < 2)
  Inertia Note: Name the specific Tier {tier} decision that would proceed unvalidated if this
    namespace is eventually MOCK-ACCEPTED. Generic statement = INERTIA-UNSPECIFIED.
    This note propagates to the Decision Authority Cost-of-MOCK field.

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary observation = ARCH-IMPLAUSIBLE (no decision label — observation only)
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  bypass-error-code: ARCH-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Arch-blocked (CONTRADICTS-ARCHITECTURE):
      [{namespace list}]
      If empty: "Arch-blocked: [] (none — all remaining namespaces proceed to Strategy Evaluation)"
    Proceeding to Strategy Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to Strategy Evaluation: [] (none)"

DO NOT proceed to STEP 4 until Architect verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table from STEP 3, adding Strategy columns for qualifying rows:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
        [Becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Score: {0|1|2|3} — must appear before Strategy Verdict. Named error: SCORE-AFTER-VERDICT.
  Strategy Verdict: ADEQUATE FOR TIER {tier} (Score >= 2)  or  INSUFFICIENT FOR TIER {tier} (Score < 2)

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary observation = STRATEGY-INADEQUATE (no decision label — observation only)
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
  Record — REQUIRED OUTPUT even when list is empty:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}):
      [{namespace list}]
      If empty: "Strategy-blocked: [] (none — all remaining namespaces proceed to PM Evaluation)"
    Proceeding to PM Evaluation:
      [{namespace list}]
      If all blocked: "Proceeding to PM Evaluation: [] (none)"

DO NOT proceed to STEP 5 until Strategy verdicts and BOTH guard records are written
(even if one or both lists are empty).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

Continue evaluation table, adding PM columns for qualifying rows:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        — or: "Absent — name the missing element and which section defines it".
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

  PM Score: {0|1|2|3} — must appear before PM Verdict. Named error: SCORE-AFTER-VERDICT.
  PM Verdict: STRUCTURALLY ADEQUATE (Score >= 2)  or  STRUCTURALLY INCOMPLETE (Score < 2)

DO NOT proceed to COVERAGE SCORE TABLE until PM verdicts are written for every qualifying namespace.

COVERAGE SCORE TABLE (emit before ROLE-SEPARATION GATE):
  | Namespace | Arch Score | Strategy Score | PM Score | Lowest Score | Preliminary |
  |-----------|-----------|---------------|---------|-------------|-------------|
  | {name}    | {0-3}     | {0-3}         | {0-3}   | {min}       | MA or RR    |
  Auto-flagged rows: omit from table (decisions fixed by rule).
  Arch-blocked rows: show Arch Score; Strategy = N/A; PM = N/A.
  Strategy-blocked rows: show Arch + Strategy Score; PM = N/A.
  Preliminary: MA = MOCK-ACCEPTED candidate (all scores >= 2); RR = REAL-REQUIRED (any score < 2).

===================================================================
ROLE-SEPARATION GATE — COVERAGE ANALYST WORK COMPLETE
Gate check (required before Decision Authority begins):
  Confirm: Zero MOCK-ACCEPTED labels appear in Steps 1–5 output.
  Confirm: Zero REAL-REQUIRED labels appear in Steps 1–5 output.
  Confirm: Inertia Note is present for every non-auto-flagged namespace.
  Confirm: Score field precedes Verdict for every evaluated namespace.
  Named error: ANALYST-PREMATURE-DECISION if any decision label found.
  Named error: INERTIA-NOTE-MISSING if any non-auto namespace lacks an Inertia Note.
  Named error: SCORE-AFTER-VERDICT if any Score field follows its Verdict.
  "Coverage Analyst work complete: {N} namespaces observed, {N_auto} auto-flagged,
   {N_arch_blocked} arch-blocked, {N_strat_blocked} strategy-blocked,
   {N_qualifying} qualifying for PM evaluation.
   Inertia Notes: {N_notes} recorded. Coverage Scores: {N_scores} recorded."
===================================================================

===================================================================
DECISION AUTHORITY ROLE — STEP 6
Role instruction: Work from Coverage Analyst observations, scores, and Inertia Notes only.
DO NOT re-read {mock-artifact-path} in this role. Named error: AUTHORITY-REREAD.
===================================================================

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
| 4     | Failing verdict: {full verdict string}     | Contrast (SLOT 2 — write first):                     |
| 5     | SQ answer driving verdict (+ Error-code)   |   [Unlike {namespace type}...]                       |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Verify: all 7 field rows above are mapped before filling either template.
Count: 7 rows defined. Confirm 7 rows present before proceeding.

MOCK-ACCEPTED template (WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Cost-of-MOCK: [From Coverage Analyst Inertia Note — name the specific Tier {tier} decision
    that proceeds without real-data validation if this namespace stays MOCK-ACCEPTED.
    If Inertia Note was INERTIA-UNSPECIFIED, supply the named decision now.
    Generic statement without named tier decision = COST-UNSPECIFIED. Error-code: COST-UNSPECIFIED.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  Failing score: [{0|1} — the score that caused the binary threshold to fail]
  SQ answer driving verdict:
    Claim: [write the SQ answer sentence here — present-tense]
    Subject-check: Identify the grammatical subject of your Claim sentence.
      If subject = role name (e.g., "Architect", "PM", "Strategy") → Error-code: VERDICT-ECHO
      If subject = artifact, section, or field (e.g., "Section 4.1", "The mock") → Error-code: NONE
    Error-code: [VERDICT-ECHO | NONE — based on Subject-check result above]
    SUBJECT-CHECK EXAMPLES TABLE:
      | Branch       | Claim form                                      | Error-code   |
      |--------------|------------------------------------------------|--------------|
      | VERDICT-ECHO | "Architect found no gate"                      | VERDICT-ECHO |
      | NONE         | "Section 4.1 contains no tier-boundary gate"   | NONE         |
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]
  Inertia validation: [Without real data for this namespace, the team proceeds without
    [name the specific unvalidated tier decision — from Coverage Analyst Inertia Note if present].
    Lift condition: [name the exact structural change that would make MOCK sufficient for Tier {tier}.]
    Generic lift condition without named structural change = LIFT-UNSPECIFIED.]

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

CANARY TERMINOLOGY TABLE (read before branch definitions; do not skip):
  | Term                  | Type            | Meaning                                                |
  |-----------------------|-----------------|--------------------------------------------------------|
  | CANARY SUPPRESSED     | Correct output  | Edits incomplete; disclosure emitted; not an error     |
  | CANARY-FALSE-POSITIVE | Named error     | Assertion emitted when condition is false; wrong claim |

  ENFORCEMENT NOTE:
    Rule: Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    Distinction: CANARY SUPPRESSED = correct disclosure of incomplete edits (not an error).
                 CANARY-FALSE-POSITIVE = assertion emitted when condition is false (named error).
    Violation: Emitting CANARY ASSERTION when one or more Status fields remain as
               "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as named error.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## Predicted Criterion Coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Basis |
|-----------|------|------|------|------|------|-------|
| C-01 FORBIDDEN OUTPUTS TRIAD | PASS | PASS | PASS | PASS | PASS | All variations carry Phase Gate verbatim |
| C-02 Triad labels present | PASS | PASS | PASS | PASS | PASS | All three labels named in Phase Gate |
| C-03 Status write-back + CANARY | PASS | PASS | PASS | PASS | PASS | STEP 8 in all variations; Edit tool + CANARY GATE |
| C-04 Review artifact structure | PASS | PASS | PASS | PASS | PASS | STEP 7 in all variations; 4-column table + P1/P2/P3 |
| C-05 Two-slot MOCK-ACCEPTED | PASS | PASS | PASS | PASS | PASS | STEP 6 MOCK-ACCEPTED template; Slot 2 before Slot 1 |
| C-06 Entity-naming grammar | PASS | PASS | PASS | PASS | PASS | "Yes/no answers do not satisfy" in all SQ blocks |
| C-07 Two-list partition + guards | PASS | PASS | PASS | PASS | PASS | ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS in all |
| C-08 REAL-REQUIRED template complete | PASS | PASS | PASS | PASS | PASS | STEP 6 evaluation-driven template in all; 5 variations |
| C-17 SUBJECT OF EVALUATION field | PASS* | PASS* | PASS* | PASS* | PASS* | *Inherited from R5 base via DEFAULT DECISION POSITION |
| C-18 CANARY TERMINOLOGY TABLE | PASS | PASS | PASS | PASS | PASS | STEP 8 in all variations; table present |
| C-19 Subject-check metacognitive step | PASS | PASS | PASS | PASS | PASS | STEP 6 REAL-REQUIRED template; Claim + Subject-check + Error-code |
| C-20 SUBJECT-CHECK EXAMPLES TABLE | PASS | PASS | PASS | PASS | PASS | 2-row table in STEP 6 REAL-REQUIRED template all variations |
| C-21 Enforcement prose after table | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT NOTE block in STEP 8 all variations |
| C-22 Count-anchored assertion after CROSS-TEMPLATE | PASS | PASS | PASS | PASS | PASS | "Count: 7 rows defined. Confirm 7 rows present." in STEP 6 all variations |
| C-23 Named Violation: field in ENFORCEMENT NOTE | PASS | PASS | PASS | PASS | PASS | Violation: field in STEP 8 ENFORCEMENT NOTE all variations |
| C-24 Role-separation gate (candidate) | PASS | FAIL | FAIL | PASS | PASS | V-01, V-04, V-05 have ROLE-SEPARATION GATE; V-02/V-03 do not |
| C-25 Per-namespace inertia cost (candidate) | FAIL | PASS | FAIL | PASS | PASS | V-02, V-04, V-05 have Cost-of-MOCK field; V-01/V-03 do not |
| C-26 Numeric pre-decision score (candidate) | FAIL | FAIL | PASS | FAIL | PASS | V-03, V-05 have Score: {0-3} per role + COVERAGE SCORE TABLE |

*Note on C-17: R5 V-05 adds a SUBJECT OF EVALUATION: line per namespace before the decision block.
R6 variations inherit the DEFAULT DECISION POSITION framing but do not pre-print a per-namespace
`SUBJECT OF EVALUATION:` line. C-17 assessment is PARTIAL for all R6 variations unless the labeled
field is added explicitly. This is a known regression from R5 V-05 in R6 single-axis variations.
V-05 full integration restores C-17 via the Coverage Analyst role instruction header.

---

## Excellence Signals — Round 6 Design

### E-1: Role separation is orthogonal to all existing criteria

The Coverage Analyst / Decision Authority split does not change any existing structural
element — it adds a gate between STEP 5 and STEP 6. The gate fires a named error
(ANALYST-PREMATURE-DECISION) if any decision label appears in Coverage Analyst output.
This is a pure addition, not a modification. It can be added to any prior variation without
affecting C-01 through C-23 scores. Predicted C-24 mechanism: "Role-separation gate present
with named error for premature decision labels."

### E-2: Inertia framing establishes a causal chain between tier decision and coverage choice

V-02 and V-04/V-05 add Cost-of-MOCK and Inertia validation fields that name the specific
tier decision affected by the coverage choice. This creates a causal chain: namespace ->
coverage decision -> tier decision consequence. This is qualitatively richer than the current
Slot 1 requirement (name a tier decision), because it requires naming the decision in both
directions (what is validated if MOCK-ACCEPTED, what is deferred if REAL-REQUIRED).
Predicted C-25 mechanism: "Cost-of-MOCK field present in MOCK-ACCEPTED template naming
the specific Tier N decision that proceeds without real validation."

### E-3: Numeric scoring surfaces partial-coverage cases the binary verdict cannot distinguish

V-03 and V-05 distinguish Score=2 (adequate) from Score=3 (strong) at the input to a binary
verdict. This preserves the binary decision gate (adequate/inadequate) while adding a
signal about confidence level within the adequate range. A coverage score table before STEP 6
provides the first single-view summary of per-namespace evidence strength. Predicted C-26
mechanism: "Per-dimension coverage scores present (Arch / Strategy / PM, scale 0-3) with
scores preceding binary verdicts and COVERAGE SCORE TABLE emitted before decision step."

### E-4: Triple-axis V-05 as ceiling probe

V-05 probes whether the three new axes can coexist without length-pressure degradation of
prior criteria. The key risk is the COVERAGE SCORE TABLE (new) plus ROLE-SEPARATION GATE
(new) plus Cost-of-MOCK fields (new) creating a prompt body long enough that a model
truncates either the SUBJECT-CHECK EXAMPLES TABLE (C-20) or the CROSS-TEMPLATE RELATIONSHIP
BLOCK (C-22). If V-05 passes C-20 and C-22 without truncation, the triple combination is
the new ceiling form. If truncation is observed, the binding constraint is identified and
V-04 (dual-axis, no scoring table) is the more reliable form.

```json
{"top_score_predicted": "108.75 (all C-01-C-23) or higher if C-24/C-25/C-26 extracted", "all_essential_pass": true, "new_patterns": ["Role-separation gate (ANALYST-PREMATURE-DECISION) creates checkable structural property: no decisions before gate fires", "Per-namespace Cost-of-MOCK field names specific tier decision consequence of coverage choice — causal chain from namespace to tier decision", "Numeric pre-decision coverage score (0-3 per dimension) preserves binary verdict threshold while adding confidence signal; COVERAGE SCORE TABLE provides single-view before decision step"]}
```
