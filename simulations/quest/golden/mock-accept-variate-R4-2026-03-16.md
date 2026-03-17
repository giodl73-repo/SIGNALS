---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-16
round: 4
rubric_version: v4
status: VARIATE
---

# mock-accept Variate — Round 4

**Date:** 2026-03-16
**Skill:** mock-accept
**Rubric:** v4 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-19 aspirational;
             C-17/C-18/C-19 new this round)
**Baseline:** R3 champion (V-05: SKIP table + Slot-2-first + bypass-error-code + two-branch
             CANARY gate + explicit empty blocked-lists + VERDICT-ECHO Error-code field +
             CANARY SUPPRESSED positive reframe + non-conflation statement)
**Round:** R4 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R3 converged on all three C-14/C-15/C-16 aspirational criteria. V-05 carries all forward.
R3 V-05 also embedded C-17/C-18/C-19 patterns as prose, but not as parseable or labeled
structures. R4 targets each new criterion by promoting its pattern from embedded prose to
explicit structural form: a labeled field, a dedicated table, or a metacognitive self-check.

| Plan | Axis | Source criterion | What changes from R3 V-05 | Predicted |
|------|------|-----------------|--------------------------|-----------|
| V-01 | lifecycle-emphasis | C-17: CANARY SUPPRESSED labeled semantics | BRANCH B gains a `Semantics:` field explicitly declaring success state: "Semantics: SUCCESS — disclosure output, not error" as a parseable label, not only embedded prose. The positive reframe becomes a checkable field rather than a sentence. | C-17 pass at maximum strength; C-18 maintained |
| V-02 | output-format | C-18: Dedicated disambiguation table before branches | Insert a CANARY TERMINOLOGY TABLE (2-row structured table) between the REPLACE block and BRANCH A/B definitions. Table rows: CANARY SUPPRESSED / CANARY-FALSE-POSITIVE with Type, Condition, Correct output columns. Separates non-conflation from the instruction prose surrounding it. | C-18 pass; C-17 maintained from R3 base |
| V-03 | phrasing-register | C-19: Self-scoring metacognitive step on Error-code | Before writing Error-code, model is instructed to identify the grammatical subject of its Claim sentence in a named sub-step. Subject identification makes the NONE vs VERDICT-ECHO distinction an explicit check, not a passive application. | C-19 pass at maximum precision; correct NONE emission increased |
| V-04 | lifecycle-emphasis + output-format | C-17 + C-18 | Combines V-01 labeled semantics field + V-02 disambiguation table. Non-overlapping: V-01 changes BRANCH B content; V-02 inserts a table before branches. | Both C-17 and C-18 pass; no mutual interference |
| V-05 | lifecycle-emphasis + output-format + phrasing-register | C-17 + C-18 + C-19 | Full R4 integration: labeled Semantics field + disambiguation table + metacognitive subject check + all R3 bases. Candidate R4 golden prompt if scoring confirms hypothesis. | All three new aspirational criteria pass; composite >= 90 |

---

## V-01 — Lifecycle Emphasis: CANARY SUPPRESSED as Labeled Semantics Field

**axis:** lifecycle-emphasis
**hypothesis:** R3 V-05 BRANCH B states "CANARY SUPPRESSED is not an error — it is the
correct disclosure output when edits are incomplete" as prose. C-17 requires the positive
reframe as a distinct, checkable declaration — not merely embedded in surrounding text.
A model scoring PARTIAL on C-17 may recognize the phrase but not emit it as a distinct
labeled output. Adding a `Semantics:` field inside BRANCH B makes the positive reframe
parseable: it can be checked as a field, not just searched as prose. The field also
reinforces that CANARY SUPPRESSED is a SUCCESS mode, which directly addresses C-17.
Failure condition: if C-17 pass rate does not improve, the criterion was already satisfied
by the prose form and the labeled field adds no incremental signal.

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
    Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.
    Do NOT emit CANARY ASSERTION when in BRANCH B.
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-02 — Output Format: CANARY Terminology Disambiguation Table

**axis:** output-format
**hypothesis:** R3 V-05 BRANCH B embeds the non-conflation instruction as a prose sentence:
"Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct
suppression." A model scoring PARTIAL on C-18 can reproduce this instruction without
structurally distinguishing the two terms. C-18 requires explicit non-conflation at the
level of a checkable output. Inserting a CANARY TERMINOLOGY TABLE before the branch
definitions separates the disambiguation from instruction prose: two rows, three columns
(Term, Type, Meaning) force the model to declare each term's category independently.
The table becomes a parseable structure that cannot be skipped by summarizing both terms
in one sentence. Failure condition: if C-18 pass rate does not improve, the inline instruction
is already sufficient and structural separation adds no incremental signal.

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
    Do NOT emit CANARY ASSERTION when in BRANCH B.
    CANARY SUPPRESSED is not an error — it is the correct disclosure output when edits are incomplete.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

## V-03 — Phrasing Register: Metacognitive Subject-Check on Error-code

**axis:** phrasing-register
**hypothesis:** R3 V-05 adds the Error-code field with a Note explaining VERDICT-ECHO vs valid
form. A model can reproduce this field mechanically by defaulting to NONE without actually
checking the grammatical subject. C-19 requires the conditional to be applied correctly —
specifically the NONE branch must fire when the artifact is the subject, not just when
VERDICT-ECHO seems absent. Adding a metacognitive sub-step — "Before writing Error-code,
identify the grammatical subject of your Claim sentence" — forces explicit subject identification
before field emission. This makes the NONE branch a deliberate output, not a default. The
self-check is framed as a named sub-step (Subject-check:) inside the SQ answer block.
Failure condition: if C-19 pass rate does not improve, the model already performs implicit
subject identification and the explicit check adds no signal.

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

---

## V-04 — Combination: Labeled Semantics + Disambiguation Table (C-17 + C-18)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** V-01 (Semantics: labeled field in BRANCH B) and V-02 (CANARY TERMINOLOGY TABLE
before branches) target the same STEP 8 section but at different locations: V-01 adds a field
inside BRANCH B; V-02 inserts a table before both branches. They do not conflict because the
table is pre-branch context and the Semantics field is intra-branch annotation. Together they
strengthen both C-17 (labeled positive reframe) and C-18 (structured non-conflation). C-19
is not targeted; Error-code with Note is carried from R3 V-05 base. Predicted composite:
C-17 and C-18 pass together, no regression on C-19 or any essential criteria.

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

## V-05 — Full R4 Integration: C-17 + C-18 + C-19 (All New Aspirational Criteria)

**axis:** lifecycle-emphasis + output-format + phrasing-register
**hypothesis:** V-01 (Semantics: labeled field, BRANCH B), V-02 (CANARY TERMINOLOGY TABLE
before branches), and V-03 (Subject-check metacognitive step in Error-code) target
non-overlapping locations: BRANCH B body, pre-branch table, and STEP 6 template schema.
All three changes plus all R3 bases compose without mutual interference. Predicted composite:
all three new aspirational criteria (C-17, C-18, C-19) pass simultaneously alongside all
essential and recommended criteria. This is the candidate R4 golden prompt if scoring confirms
the hypothesis.

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
