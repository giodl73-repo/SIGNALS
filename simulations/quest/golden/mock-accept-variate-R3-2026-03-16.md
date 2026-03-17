---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-16
round: 3
rubric_version: v3
status: VARIATE
---

# mock-accept Variate — Round 3

**Date:** 2026-03-16
**Skill:** mock-accept
**Rubric:** v3 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-16 aspirational;
             C-14/C-15/C-16 new this round)
**Baseline:** R2 champion (V-05: SKIP table + Slot-2-first + bypass-error-code fields)
**Round:** R3 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R2 converged on three mechanisms: SKIP table (C-13), Slot 2 before Slot 1 (C-12),
and bypass-error-code fields in guard records (C-11). All three carry forward as the
established base. R3 targets the three new aspirational criteria extracted from R2
scorecard excellence signals.

| Plan | Axis | Source criterion | What changes | Predicted |
|------|------|-----------------|--------------|-----------|
| V-01 | lifecycle-emphasis | C-14: CANARY SUPPRESSED branch | Step 8 restructured as a two-branch gate (BRANCH A / BRANCH B) with CANARY-SUPPRESSED-PATH named as a distinct output mode separate from CANARY-FALSE-POSITIVE | C-14 pass; C-03 maintained (Edit tool still required) |
| V-02 | output-format | C-15: Empty blocked-list explicit | Guard records in STEP 3 and STEP 4 require explicit empty-list notation when no namespaces are blocked; "Arch-blocked: [] (empty)" becomes a required output even when the list has zero members | C-15 pass; C-07 maintained (partition still required) |
| V-03 | phrasing-register | C-16: VERDICT-ECHO as error code | Row 5 of STEP 6 promoted from prose constraint to named parseable field in the REAL-REQUIRED template; template gains an Error-code field with enumerated values including VERDICT-ECHO | C-16 pass; C-08 maintained (full template still required) |
| V-04 | lifecycle-emphasis + output-format | C-14 + C-15 | Combines V-01 two-branch CANARY gate + V-02 explicit empty-list notation; non-overlapping changes that target separate steps | Both C-14 and C-15 pass; no mutual interference expected |
| V-05 | lifecycle-emphasis + output-format + phrasing-register | C-14 + C-15 + C-16 | Full R3 integration: two-branch CANARY + explicit empty blocked-lists + VERDICT-ECHO parseable error code + all R2 bases carried forward | All three new aspirational criteria pass; composite >= 85 |

---

## V-01 — Lifecycle Emphasis: CANARY SUPPRESSED as Named Two-Branch Gate

**axis:** lifecycle-emphasis
**hypothesis:** The current baseline mentions CANARY SUPPRESSED inline as an else-clause
("If condition not met: output 'CANARY SUPPRESSED...'"). This prose proximity to
CANARY-FALSE-POSITIVE creates a naming conflation risk — a model may treat suppression
as the error rather than as the correct alternative path. Restructuring Step 8 as an
explicit two-branch gate (BRANCH A — assertion path; BRANCH B — suppression path) with
each branch named and each error named distinctly prevents conflation. CANARY-FALSE-POSITIVE
is an error (assertion emitted when fields remain). CANARY SUPPRESSED is not an error —
it is the correct output when edits are incomplete. Making that distinction structural
rather than prose should produce C-14 PASS without touching C-03 (Edit tool still fires).
Failure condition: if C-14 pass rate does not improve, the conflation is not the cause —
the model may be failing to edit rather than failing to label.

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
  Record (required even if list is empty):
    Arch-blocked (CONTRADICTS-ARCHITECTURE): [{list} | empty — write "Arch-blocked: []"]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 until Architect verdicts and guard assignments are complete.

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
  Record (required even if list is empty):
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}): [{list} | empty — write "Strategy-blocked: []"]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete.

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
| 5     | SQ answer driving verdict:                 |   [Unlike {namespace type}, which carries            |
|       |   {artifact-as-subject form}               |   {structural factor}...]                            |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
|       |                                            |   [SQ-1 anchor — Tier {tier} decision]               |
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

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).
    CANARY-FALSE-POSITIVE = assertion emitted when condition is false.

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Do NOT emit CANARY ASSERTION when in BRANCH B.
    CANARY SUPPRESSED is not an error — it is the correct output when edits are incomplete.
    Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE.
    CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression with disclosure.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one]

---

## V-02 — Output Format: Empty Blocked-Lists Stated Explicitly

**axis:** output-format
**hypothesis:** The current baseline records guard output as "Arch-blocked: [{list}]" when
namespaces are blocked, but does not specify the required output when the list is empty.
A model skips the record entirely when no namespaces are blocked, producing silence where
an explicit "Arch-blocked: [] (none)" is required for C-15. Adding an explicit format
constraint — "{list} | empty — write 'Arch-blocked: []'" — in both STEP 3 and STEP 4
guards forces the model to produce the record unconditionally, not only when items exist.
This is an output-format change: the schema of the guard record changes, not the logic.
Failure condition: if C-15 pass rate does not improve despite the format constraint,
the model is treating the empty case correctly through inference and C-15 is satisfiable
by the baseline without this change.

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
      If all blocked: "Proceeding to Strategy Evaluation: [] (none — all remaining are Arch-blocked)"

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
      If all blocked: "Proceeding to PM Evaluation: [] (none — all remaining are Strategy-blocked)"

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
| 5     | SQ answer driving verdict:                 |   [Unlike {namespace type}, which carries            |
|       |   {artifact-as-subject form}               |   {structural factor}...]                            |
| 6     | Artifact state: {art-subj, pres-tense}     | Structural position (SLOT 1 — write second):         |
|       |                                            |   [SQ-1 anchor — Tier {tier} decision]               |
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

## V-03 — Phrasing Register: VERDICT-ECHO as Named Parseable Error Code in Template

**axis:** phrasing-register
**hypothesis:** The current baseline mentions "ERROR — VERDICT-ECHO: role as subject" as an
inline prose constraint on Row 5 of the REAL-REQUIRED template. A model can satisfy the
prose without emitting VERDICT-ECHO as a parseable, checkable field. C-16 requires
VERDICT-ECHO to appear as a named error code in the template output — not only as an
instruction. Promoting Row 5 from a grammar constraint to a structured field with an
explicit Error-code: line makes VERDICT-ECHO a checkable artifact field, not just a
reminder. The change affects phrasing-register: the imperative shifts from instruction to
schema. Failure condition: if C-16 pass rate does not improve, the model is already
treating VERDICT-ECHO as an output constraint; the criterion may be already achievable
by the baseline.

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
  Record:
    Arch-blocked (CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 until Architect verdicts and guard assignments are complete.

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
  Record:
    Strategy-blocked (INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete.

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
| 5     | SQ answer driving verdict:                 |   [Unlike {namespace type}...]                       |
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
    Claim: [present-tense, artifact as grammatical subject]
    Error-code: [VERDICT-ECHO if role is grammatical subject | NONE if artifact is subject]
    Note: VERDICT-ECHO = error. "Architect found no gate" is VERDICT-ECHO.
          "Section 4.1 contains no tier-boundary gate" is valid (artifact as subject).
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

## V-04 — Combination: CANARY SUPPRESSED Branch + Empty Blocked-Lists (C-14 + C-15)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** V-01 (CANARY SUPPRESSED explicit branch) and V-02 (empty blocked-lists
stated explicitly) target different steps (Step 8 and Steps 3/4 respectively) with
non-overlapping schema changes. Combining them should produce independent C-14 and C-15
passes without mutual interference: the two-branch CANARY gate does not affect guard
record format, and the empty-list guard constraint does not affect the CANARY output path.
Predicted composite improvement over R2 champion: +2 aspirational criteria (C-14, C-15).
C-16 not targeted; VERDICT-ECHO remains as prose instruction only.

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
| 5     | SQ answer driving verdict:                 |   [Unlike {namespace type}...]                       |
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

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Do NOT emit CANARY ASSERTION when in BRANCH B.
    CANARY SUPPRESSED is not an error — it is the correct disclosure output.
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one]

---

## V-05 — Full R3 Integration: C-14 + C-15 + C-16 (All New Aspirational Criteria)

**axis:** lifecycle-emphasis + output-format + phrasing-register
**hypothesis:** V-01 (two-branch CANARY gate), V-02 (explicit empty blocked-list records),
and V-03 (VERDICT-ECHO as parseable error code field) target non-overlapping locations:
Step 8, Steps 3/4 guard records, and Step 6 template schema. All three changes plus all
R2 bases (SKIP table, Slot-2-first, bypass-error-code fields) should compose without
mutual interference. Predicted composite: all three new aspirational criteria (C-14,
C-15, C-16) pass simultaneously alongside existing essential and recommended criteria.
This is the candidate R3 golden prompt if scoring confirms the hypothesis.

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
    Claim: [present-tense, artifact as grammatical subject]
    Error-code: [VERDICT-ECHO if role is grammatical subject | NONE if artifact is subject]
    Note: VERDICT-ECHO = error. "Architect found no gate" = VERDICT-ECHO (role as subject).
          "Section 4.1 contains no tier-boundary gate" = valid (artifact as subject, NONE).
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

CANARY GATE — two branches, mutually exclusive. Determine which branch applies:

  BRANCH A — CANARY ASSERTION PATH (all Status fields successfully updated):
    Condition: zero Status fields remain as "MOCK (awaiting review)".
    Required output: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
    Named error: CANARY-FALSE-POSITIVE — PROHIBITED if any field remains as MOCK (awaiting review).
    CANARY-FALSE-POSITIVE = assertion emitted when the condition is false.

  BRANCH B — CANARY SUPPRESSED PATH (one or more Status fields not updated):
    Condition: one or more Status fields still read "MOCK (awaiting review)" after edit attempts.
    Required output: "CANARY SUPPRESSED: {N} field(s) not updated — {namespace list}"
    Do NOT emit CANARY ASSERTION when in BRANCH B.
    CANARY SUPPRESSED is not an error — it is the correct disclosure output when edits are incomplete.
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]
