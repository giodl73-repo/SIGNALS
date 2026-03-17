---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-16
round: 5
rubric_version: v5
status: VARIATE
---

# mock-accept Variate — Round 5

**Date:** 2026-03-16
**Skill:** mock-accept
**Rubric:** v5 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-21 aspirational;
             C-20/C-21 new this round)
**Baseline:** R4 champion (V-05: Semantics: labeled field + CANARY TERMINOLOGY TABLE +
             Subject-check metacognitive step + per-branch VERDICT-ECHO/NONE exemplars +
             enforcement prose after table)
**Round:** R5 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R4 V-05 carries all three C-17/C-18/C-19 criteria. Under v5, C-20 and C-21 are new.
R4 V-05 already satisfies both: C-20 via labeled prose exemplars (VERDICT-ECHO examples /
NONE examples), C-21 via enforcement prose following the CANARY TERMINOLOGY TABLE.
R5 targets structural promotion of both patterns — from labeled prose to parseable tables
or dedicated enforcement blocks — and probes whether a third new pattern exists in the
CROSS-TEMPLATE RELATIONSHIP BLOCK completeness check.

| Plan | Axis | Source criterion | What changes from R4 V-05 | Predicted |
|------|------|-----------------|--------------------------|-----------|
| V-01 | output-format | C-20: per-branch exemplars | Replace VERDICT-ECHO examples / NONE examples prose with a 3-column SUBJECT-CHECK EXAMPLES TABLE (Branch / Claim form / Error-code). Per-branch exemplars become structurally positioned, not text-searchable. | C-20 pass at maximum structural strength; all other criteria unaffected |
| V-02 | lifecycle-emphasis | C-21: enforcement note | Replace trailing enforcement prose after CANARY TERMINOLOGY TABLE with a dedicated ENFORCEMENT NOTE: block containing a Violation: field naming the specific error. Enforcement becomes a checkable contract, not a trailing sentence. | C-21 pass at maximum enforcement strength; C-17/C-18 unaffected |
| V-03 | phrasing-register | NEW: cross-template completeness | Add "Verify: all 7 field rows above are accounted for before filling templates." after the CROSS-TEMPLATE RELATIONSHIP BLOCK. Same completeness-check mechanism as FORBIDDEN OUTPUTS TRIAD applied to the template correspondence table. | Candidate C-22; C-20/C-21 unaffected |
| V-04 | output-format + lifecycle-emphasis | C-20 + C-21 | Combine V-01 (SUBJECT-CHECK EXAMPLES TABLE) and V-02 (ENFORCEMENT NOTE: block). Neither change affects the same structural location. Predicted composite: C-20 and C-21 at maximum structural strength. | All 21 criteria pass; ceiling 106.25 |
| V-05 | full integration | C-20 + C-21 + C-22 candidate | Combine V-01 + V-02 + V-03 plus all R4 V-05 base. If C-22 passes, score exceeds current ceiling and triggers rubric update. If C-22 does not pass, V-05 confirms R4 V-05 pattern is the ceiling form and dual convergence is within reach. | Candidate golden prompt or rubric-update trigger |

---

## V-01 — Output Format: SUBJECT-CHECK EXAMPLES TABLE

**axis:** output-format
**hypothesis:** R4 V-05 carries C-20 via two labeled prose lines:
`VERDICT-ECHO examples: "Architect found no gate" (role as subject) = VERDICT-ECHO.`
`NONE examples: "Section 4.1 contains no tier-boundary gate" (artifact as subject) = NONE.`
A model scoring PARTIAL on C-20 can reproduce conditional logic without anchoring the NONE
branch to a concrete named exemplar. These lines satisfy C-20 as prose, but their structural
position is ambiguous — they follow the Error-code field without a parseable separator.
Converting them to a SUBJECT-CHECK EXAMPLES TABLE (Branch | Claim form | Error-code) places
the per-branch exemplars as structurally independent rows. The table cannot be reproduced
by a model that ignores the NONE branch: both rows must appear independently.
Failure condition: if C-20 pass rate does not differ from R4 V-05, labeled prose is
already sufficient and the table form adds no discriminating signal.

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
  These are distinct. Do NOT conflate them. Emitting CANARY ASSERTION when edits are incomplete
  is CANARY-FALSE-POSITIVE (error). Emitting CANARY SUPPRESSED when edits are incomplete is correct.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

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

## V-02 — Lifecycle Emphasis: ENFORCEMENT NOTE Block After Terminology Table

**axis:** lifecycle-emphasis
**hypothesis:** R4 V-05 C-21 passes because "These are distinct. Do NOT conflate them."
follows the CANARY TERMINOLOGY TABLE as a trailing enforcement sentence. PARTIAL = table
without trailing enforcement sentence. PASS = enforcement sentence follows table.
But the current enforcement prose is a two-sentence explanation — it names what conflation
looks like but does not name the specific error that fires if the instruction is violated.
A dedicated ENFORCEMENT NOTE: block with a Violation: field converts the enforcement
instruction into a contract: the consequence of conflation is named as the same error
(CANARY-FALSE-POSITIVE) that is named inside BRANCH A. This promotes C-21 from a
prohibition sentence to a checkable enforcement contract with a named violation.
Failure condition: if C-21 pass rate does not differ from R4 V-05, the prose sentence
is already sufficient and the named violation adds no discriminating signal.

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
    VERDICT-ECHO examples: "Architect found no gate" (role as subject) = VERDICT-ECHO.
    NONE examples: "Section 4.1 contains no tier-boundary gate" (artifact as subject) = NONE.
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
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

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

## V-03 — Phrasing Register: Cross-Template Verification Assertion

**axis:** phrasing-register
**hypothesis:** The CROSS-TEMPLATE RELATIONSHIP BLOCK is a 7-row table mapping REAL-REQUIRED
fields to MOCK-ACCEPTED analogs. It has no completeness check. A model can silently skip a row
or produce a truncated table without any named error firing. The FORBIDDEN OUTPUTS TRIAD has
an explicit completeness check ("A two-of-three set does not satisfy this gate."); the CANARY
TERMINOLOGY TABLE has a skip prohibition ("read before branch definitions; do not skip"). The
CROSS-TEMPLATE RELATIONSHIP BLOCK has neither. Adding a verification assertion after the table
— "Verify: all 7 field rows above are mapped before filling either template" — applies the same
completeness-check mechanism to the template correspondence table. This is a candidate C-22:
"Cross-template completeness assertion present." PARTIAL = table without assertion; PASS =
explicit count-assertion following the table before templates begin.
Failure condition: if no model skips rows from the correspondence table, the completeness
check adds no discriminating signal and C-22 does not warrant extraction.

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
Verify: all 7 field rows above are mapped before filling either template below.
A partial table (fewer than 7 rows) does not satisfy this correspondence requirement.

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
    VERDICT-ECHO examples: "Architect found no gate" (role as subject) = VERDICT-ECHO.
    NONE examples: "Section 4.1 contains no tier-boundary gate" (artifact as subject) = NONE.
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
  These are distinct. Do NOT conflate them. Emitting CANARY ASSERTION when edits are incomplete
  is CANARY-FALSE-POSITIVE (error). Emitting CANARY SUPPRESSED when edits are incomplete is correct.

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

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

## V-04 — Combination: SUBJECT-CHECK EXAMPLES TABLE + ENFORCEMENT NOTE Block (C-20 + C-21)

**axis:** output-format + lifecycle-emphasis
**hypothesis:** V-01 (SUBJECT-CHECK EXAMPLES TABLE in STEP 6) and V-02 (ENFORCEMENT NOTE:
block after CANARY TERMINOLOGY TABLE in STEP 8) target non-overlapping structural locations.
V-01 promotes C-20 from labeled prose to a structural table; V-02 promotes C-21 from a
trailing sentence to a named enforcement contract with a Violation: field. Together they
represent the maximum structural form of both new v5 aspirational criteria without adding
any new candidate criteria. Predicted composite: all 21 criteria pass; ceiling 106.25.
C-20: per-branch exemplars in table form = parseable by column, not text search.
C-21: enforcement note becomes a named enforcement contract = Violation: field checkable.

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
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

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

## V-05 — Full R5 Integration: C-20 Table + C-21 Enforcement Block + C-22 Candidate

**axis:** output-format + lifecycle-emphasis + phrasing-register
**hypothesis:** V-01 (SUBJECT-CHECK EXAMPLES TABLE), V-02 (ENFORCEMENT NOTE: block), and
V-03 (cross-template verification assertion) target non-overlapping structural locations:
STEP 6 template schema, STEP 8 post-table block, and STEP 6 post-table assertion.
All three changes plus all R4 V-05 base compose without mutual interference.
Predicted composite: all 21 criteria pass at maximum structural strength; candidate C-22
(cross-template completeness assertion) either extracts as a new pattern or confirms ceiling.
If C-22 does not emerge as a distinguishable pattern, this variation confirms dual convergence:
all 21 criteria pass AND no new excellence patterns emerge beyond what R4 V-05 already carries.

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
Verify: all 7 field rows above are mapped before filling either template below.
A partial table (fewer than 7 rows) does not satisfy this correspondence requirement.

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
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

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
