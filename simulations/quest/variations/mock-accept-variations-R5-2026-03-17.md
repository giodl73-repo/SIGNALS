Good — I now have the complete R4 V-05 base (through line 1487). It ends after STEP 8 with no GATE F and no opening Standing Rule. The two gaps for R5 are confirmed: C-23 (three-step halt) and C-25 (Slot 2 paraphrase examples). GATE F (C-24) is also absent in the V-05 text — I'll add it explicitly in all R5 variations to anchor that criterion.

Now writing the 5 complete variations:

---

```markdown
---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 5
rubric_version: v5
status: VARIATE
---

# mock-accept Variate — Round 5

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v5 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-25 aspirational;
             C-23/C-24/C-25 new this round)
**Baseline:** R4 champion (V-05: SKIP table + Slot-2-first + bypass-error-code +
             two-branch CANARY gate + explicit empty blocked-lists + VERDICT-ECHO
             Error-code field + Subject-check + CANARY SUPPRESSED Semantics: field +
             CANARY TERMINOLOGY TABLE + non-conflation statement)
**Round:** R5 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R4 converged on all C-09–C-22 aspirational criteria. V-05 carries all forward. R4 V-04
scored 14/17 against v5, failing only C-23 (two-step halt, not three-step) and C-25
(Slot 2 paraphrase not extended from Slot 1 baseline). C-24 (GATE F section IDs) passed
in R4 but GATE F was implicit; R5 makes it explicit in all variations as a free base carry.

Two R4 gaps:
1. **C-23**: halt instruction in the forbidden-form enumeration is "halt and rewrite" (two
   imperatives). C-23 requires three atomic steps: HALT / DELETE / REWRITE, each as a
   separate imperative, eliminating evaluator discretion about intermediate steps.
2. **C-25**: Slot 2 revert-on-violation names the violation class ("near-miss paraphrase")
   but does not supply at least two quoted altered-token near-miss examples. C-25 requires
   quoted forms so the evaluator can match by token, not by interpretation.

| Plan | Axis | Target criterion | What changes from R4 V-05 base | Predicted |
|------|------|-----------------|-------------------------------|-----------|
| V-01 | phrasing-register | C-23 | Opening STANDING RULE block gains the three-step sequence verbatim: "HALT. Delete the violating line. Rewrite in PASS form." Forbidden-form enumeration and halt are now in one named block at top. C-25 added as prose note (not table). | C-23 PASS; C-25 borderline (prose note, no quoted forms) |
| V-02 | output-format | C-25 | Slot 2 revert-on-violation gains a dedicated SLOT 2 VIOLATION TABLE (3 rows, 2 columns: quoted near-miss form, violation type). C-23 carries the R4 borderline two-step form — isolates C-25 axis. | C-25 PASS at structural level; C-23 unchanged from R4 (borderline) |
| V-03 | lifecycle-emphasis | C-23 + C-24 | Three-step halt co-located at each constrained field site as an inline CONSTRAINT block (C-18 adjacency). GATE F named as a separate STEP 9 with explicit section IDs. C-25 not targeted. | C-23 PASS via co-location; C-24 PASS at max strength; C-25 unchanged |
| V-04 | phrasing-register + output-format | C-23 + C-25 | V-01 opening STANDING RULE (three-step halt) + V-02 Slot 2 VIOLATION TABLE. Non-overlapping: opening rule vs. STEP 6 template. | Both C-23 and C-25 PASS; composite >= 98 |
| V-05 | phrasing-register + output-format + lifecycle-emphasis | C-23 + C-24 + C-25 | Full R5: V-01 opening block + V-02 Slot 2 table + V-03 GATE F as STEP 9. All three new aspirational criteria explicitly anchored. Candidate R5 golden if scoring confirms. | 17/17 aspirational; composite = 100 |

---

## V-01 — Phrasing Register: Three-Step Halt in Opening Standing Rule

**axis:** phrasing-register
**hypothesis:** R4 V-05 has artifact-as-subject grammar embedded in templates and
evaluation notes but does not open with an explicit Standing Rule. C-23 requires the
halt instruction in the forbidden-form enumeration to name three sequential atomic
imperatives — "HALT. Delete the violating line. Rewrite in PASS form." — not the
R4 borderline form "halt and rewrite before advancing." Adding a STANDING RULE block
before STEP 1, with a three-sentence forbidden-form enumeration and the three-step
halt sequence, satisfies C-09 (standing rule at top), C-15 (forbidden alternatives
enumerated), C-20 (halt instruction), and C-23 (three-step form). C-25 is partially
addressed via a prose note at Slot 2 but without quoted altered-token examples — this
is the intentional gap to isolate the C-23 axis.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

STANDING RULE — ARTIFACT-AS-SUBJECT GRAMMAR
All output in all steps uses the mock artifact as grammatical subject.
  PASS form: "The mock artifact's [ns] section records / shows / lacks [detail]."
  Forbidden forms — do not produce:
    "I found N fields present in [ns]" — VIOLATION (evaluation-level: first person as subject)
    "This namespace has structural gaps" — VIOLATION (artifact-level: this namespace as subject)
    "The [ns] namespace shows adequate coverage" — VIOLATION (namespace-level: [ns] namespace as subject)
When a violation appears in output:
  HALT. Delete the violating line. Rewrite in PASS form.
Exempt: tier sourcing line in STEP 1; auto-flag rule definitions; role verdict labels.

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
    Revert-on-violation (Slot 2): if the Contrast sentence places the namespace or
    coverage as the grammatical subject rather than the mock artifact, it is a near-miss
    paraphrase violation. Revert Slot 2 to blank template. Rewrite in artifact-as-subject form.

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
  Section Coverage: Coverage Review table — | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Section Structural records (one line per namespace, artifact-as-subject form):
    "The mock artifact's [ns] section records / lacks [specific structural element]."

  Section Risk:
    For each REAL-REQUIRED: "[ns] URGENCY:[BLOCKING | HIGH | MEDIUM] — {decision at risk}"
    Cross-namespace: "Highest-risk gap: {namespace} — {Tier {tier} decision} — urgency: {level}"

  Section Next Steps: numbered list of required actions, one per REAL-REQUIRED namespace.
    Format: "/{skill-id} {topic} — {Artifact state}"

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
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

GATE F — COMPLETENESS CHECK:
  Verifying review artifact sections by stable IDs:
  - Coverage: [present — {N} rows | incomplete — {detail}]
  - Structural records: [present — {N} entries | incomplete — {detail}]
  - Risk: [present | incomplete — {detail}]
  - Next Steps: [present | empty — flag]
  Gate result: PASS | FAIL — {reason if FAIL}
  If FAIL: do not close skill. Return to failing section and complete before reporting done.

---

## V-02 — Output Format: Slot 2 Violation Table

**axis:** output-format
**hypothesis:** R4 V-05 carries the Slot 2 revert-on-violation instruction as prose:
"if the Contrast sentence places the namespace or coverage as the grammatical subject...
it is a near-miss paraphrase violation." C-25 requires at least two quoted altered-token
forms — near-miss examples that are unambiguously recognizable by inspection without
requiring evaluator interpretation of what "namespace as subject" means. A SLOT 2
VIOLATION TABLE with 3 rows of quoted near-miss text + violation type makes the
constraint machine-parseable: the evaluator can compare their Contrast sentence character
by character against the table rows instead of applying a grammatical rule. This change
is isolated to the STEP 6 Slot 2 block. The three-step halt is not yet added to the
opening rule (C-23 axis intentionally isolated) — the opening rule retains the R4
borderline two-step form to isolate the C-25 vs C-23 contribution.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

GRAMMAR RULE — ARTIFACT-AS-SUBJECT:
  All output uses the mock artifact as grammatical subject. PASS form:
  "The mock artifact's [ns] section records / shows / lacks [detail]."
  If a violation appears in output: halt and rewrite in PASS form before continuing.

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

    SLOT 2 VIOLATION TABLE — if any of these near-miss forms appear in your Contrast
    sentence, revert Slot 2 to blank template and rewrite:
    | Quoted near-miss form                                             | Violation type           |
    |-------------------------------------------------------------------|--------------------------|
    | "The [ns] namespace shows unlike evidence-heavy counterparts..."  | namespace-level subject   |
    | "Unlike other namespaces, coverage here is fully structural..."   | anonymous "coverage here" |
    | "This namespace's outputs differ from evidence-requiring types..."| artifact-level trigger    |
    Token match: if your Contrast sentence contains "namespace shows", "coverage here", or
    "This namespace's outputs", it matches a table row. Revert. Do not attempt to salvage.

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
  Section Coverage: Coverage Review table — | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Section Structural records (one line per namespace, artifact-as-subject form):
    "The mock artifact's [ns] section records / lacks [specific structural element]."

  Section Risk:
    For each REAL-REQUIRED: "[ns] URGENCY:[BLOCKING | HIGH | MEDIUM] — {decision at risk}"
    Cross-namespace: "Highest-risk gap: {namespace} — {Tier {tier} decision} — urgency: {level}"

  Section Next Steps: numbered list, one entry per REAL-REQUIRED namespace.
    Format: "/{skill-id} {topic} — {Artifact state}"

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
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

GATE F — COMPLETENESS CHECK:
  Verifying review artifact sections by stable IDs:
  - Coverage: [present — {N} rows | incomplete — {detail}]
  - Structural records: [present — {N} entries | incomplete — {detail}]
  - Risk: [present | incomplete — {detail}]
  - Next Steps: [present | empty — flag]
  Gate result: PASS | FAIL — {reason if FAIL}
  If FAIL: do not close skill. Return to failing section and complete before reporting done.

---

## V-03 — Lifecycle Emphasis: Three-Step Halt Co-Located at Each Constrained Field

**axis:** lifecycle-emphasis
**hypothesis:** V-01 places the three-step halt in the opening Standing Rule (top of prompt).
C-23 requires the halt sequence "at" the forbidden-form enumeration — C-20's base criterion
is the halt instruction in the same block as the enumeration (C-15). V-03 tests whether
co-locating the three-step halt instruction adjacent to each specific constrained field
(C-18 style adjacency) passes C-23 more reliably than a single upfront rule. Two locations
are targeted: (1) the reason-code field in MOCK-ACCEPTED, where the exact-token constraint
is declared; (2) each CONSTRAINT block in STEP 6. The opening rule is retained as a
lightweight grammar note (not the full three-step form) to isolate the co-location axis.
C-25 is not targeted — Slot 2 carries the prose note from V-01 to hold that variable constant.
GATE F is added as STEP 9 (explicit named step) to strengthen C-24.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

GRAMMAR RULE — ARTIFACT-AS-SUBJECT:
  All output uses the mock artifact as grammatical subject. PASS form:
  "The mock artifact's [ns] section records / shows / lacks [detail]."
  Forbidden: first-person subject ("I found"), namespace subject ("this namespace"),
  evaluation subject ("coverage shows"). Violation = rewrite before continuing.

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

  CONSTRAINT: reason-code MUST be one of the two tokens above verbatim.
  If the written reason-code is not exactly STRUCTURAL-COVERAGE-SUFFICIENT or
  DOMAIN-KNOWLEDGE-CONSISTENT:
    HALT. Delete the violating line. Rewrite in PASS form.

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.
    Revert-on-violation (Slot 2): if the Contrast sentence uses a near-miss paraphrase
    form (namespace as subject, anonymous coverage, artifact-level trigger), revert Slot 2
    to blank template and rewrite in artifact-as-subject form.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this
    namespace supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  CONSTRAINT: Slot 1 Structural position MUST name the SQ-1 decision verbatim.
  If the written Slot 1 is a generic adequacy statement without the SQ-1 decision name:
    HALT. Delete the violating line. Rewrite in PASS form.

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
  Section Coverage: Coverage Review table — | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Section Structural records (one line per namespace, artifact-as-subject form):
    "The mock artifact's [ns] section records / lacks [specific structural element]."

  Section Risk:
    For each REAL-REQUIRED: "[ns] URGENCY:[BLOCKING | HIGH | MEDIUM] — {decision at risk}"
    Cross-namespace: "Highest-risk gap: {namespace} — {Tier {tier} decision} — urgency: {level}"

  Section Next Steps: numbered list, one entry per REAL-REQUIRED namespace.
    Format: "/{skill-id} {topic} — {Artifact state}"

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
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

STEP 9 — GATE F: COMPLETENESS GATE (named step, not optional)

Before reporting done, verify all review artifact sections are complete by stable section ID:

  GATE F — Section-by-section check:
  - Section Coverage: [present — {N} namespace rows | INCOMPLETE — {detail}]
  - Section Structural records: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Risk: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Next Steps: [present — {N} entries | INCOMPLETE — {detail}]
  Total sections: {P} of 4 complete.
  Gate result: PASS (all 4 present) | FAIL ({section ID} incomplete)
  Do not proceed until written. If GATE F FAIL: return to failing section. Complete it. Recheck.

---

## V-04 — Combination: Phrasing Register + Output Format (C-23 + C-25)

**axis:** phrasing-register + output-format
**hypothesis:** V-01 (opening STANDING RULE with three-step halt: "HALT. Delete the violating
line. Rewrite in PASS form.") and V-02 (SLOT 2 VIOLATION TABLE with 3 quoted near-miss forms)
target non-overlapping locations: the opening rule block vs. the STEP 6 Slot 2 template. They
do not interfere: V-01's halt sequence fires on any grammar violation across all phases; V-02's
violation table fires specifically when writing the Slot 2 Contrast sentence. Together they
address C-23 and C-25 simultaneously. All R4 V-05 bases (C-09–C-22) are preserved. GATE F is
carried from V-03 as a named STEP 9 to anchor C-24. Predicted composite: 17/17 aspirational
= 100.0 total. If scoring falls short, the gap is likely in C-25 (whether prose note or table
structure is sufficient) or C-23 (whether opening rule location satisfies co-location intent).

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

STANDING RULE — ARTIFACT-AS-SUBJECT GRAMMAR
All output in all steps uses the mock artifact as grammatical subject.
  PASS form: "The mock artifact's [ns] section records / shows / lacks [detail]."
  Forbidden forms — do not produce:
    "I found N fields present in [ns]" — VIOLATION (evaluation-level: first person as subject)
    "This namespace has structural gaps" — VIOLATION (artifact-level: this namespace as subject)
    "The [ns] namespace shows adequate coverage" — VIOLATION (namespace-level: [ns] namespace as subject)
When a violation appears in output:
  HALT. Delete the violating line. Rewrite in PASS form.
Exempt: tier sourcing line in STEP 1; auto-flag rule definitions; role verdict labels.

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

    SLOT 2 VIOLATION TABLE — if any of these near-miss forms appear in your Contrast
    sentence, revert Slot 2 to blank template and rewrite:
    | Quoted near-miss form                                             | Violation type           |
    |-------------------------------------------------------------------|--------------------------|
    | "The [ns] namespace shows unlike evidence-heavy counterparts..."  | namespace-level subject   |
    | "Unlike other namespaces, coverage here is fully structural..."   | anonymous "coverage here" |
    | "This namespace's outputs differ from evidence-requiring types..."| artifact-level trigger    |
    Token match: if your Contrast sentence contains "namespace shows", "coverage here", or
    "This namespace's outputs", it matches a table row. Revert. Do not attempt to salvage.

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
  Section Coverage: Coverage Review table — | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Section Structural records (one line per namespace, artifact-as-subject form):
    "The mock artifact's [ns] section records / lacks [specific structural element]."

  Section Risk:
    For each REAL-REQUIRED: "[ns] URGENCY:[BLOCKING | HIGH | MEDIUM] — {decision at risk}"
    Cross-namespace: "Highest-risk gap: {namespace} — {Tier {tier} decision} — urgency: {level}"

  Section Next Steps: numbered list, one entry per REAL-REQUIRED namespace.
    Format: "/{skill-id} {topic} — {Artifact state}"

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
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

STEP 9 — GATE F: COMPLETENESS GATE (named step, not optional)

Before reporting done, verify all review artifact sections are complete by stable section ID:

  GATE F — Section-by-section check:
  - Section Coverage: [present — {N} namespace rows | INCOMPLETE — {detail}]
  - Section Structural records: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Risk: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Next Steps: [present — {N} entries | INCOMPLETE — {detail}]
  Total sections: {P} of 4 complete.
  Gate result: PASS (all 4 present) | FAIL ({section ID} incomplete)
  Do not proceed until written. If GATE F FAIL: return to failing section. Complete it. Recheck.

---

## V-05 — Full R5 Integration: All Three Axes (C-23 + C-24 + C-25)

**axis:** phrasing-register + output-format + lifecycle-emphasis
**hypothesis:** V-01 (opening STANDING RULE with three-step halt sequence), V-02 (Slot 2
VIOLATION TABLE with 3 quoted near-miss forms), and V-03 (HALT/DELETE/REWRITE co-located
at each constrained field as a framed CONSTRAINT block, plus GATE F as named STEP 9) target
three distinct locations: the opening of the prompt, the Slot 2 Contrast block, and each
CONSTRAINT field site in STEP 6. All three operate without mutual interference. Combined,
they should satisfy C-23 at maximum strength (three-step halt in opening rule + in-line at
constraint sites), C-24 at maximum strength (explicit GATE F naming all four section IDs as
stable identifiers), and C-25 at maximum strength (quoted altered-token near-miss table with
token-match instruction in Slot 2). All R4 V-05 bases (CANARY TABLE, Semantics: field,
Subject-check) are preserved. This is the candidate R5 golden prompt.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

STANDING RULE — ARTIFACT-AS-SUBJECT GRAMMAR
All output in all steps uses the mock artifact as grammatical subject.
  PASS form: "The mock artifact's [ns] section records / shows / lacks [detail]."
  Forbidden forms — do not produce:
    "I found N fields present in [ns]" — VIOLATION (evaluation-level: first person as subject)
    "This namespace has structural gaps" — VIOLATION (artifact-level: this namespace as subject)
    "The [ns] namespace shows adequate coverage" — VIOLATION (namespace-level: [ns] namespace as subject)
When a violation appears in output:
  HALT. Delete the violating line. Rewrite in PASS form.
Exempt: tier sourcing line in STEP 1; auto-flag rule definitions; role verdict labels.

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

  CONSTRAINT: reason-code MUST be one of the two tokens above verbatim.
  If the written reason-code is not exactly STRUCTURAL-COVERAGE-SUFFICIENT or
  DOMAIN-KNOWLEDGE-CONSISTENT:
    HALT. Delete the violating line. Rewrite in PASS form.

  Contrast (SLOT 2 — first to write, structurally separate from Slot 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.

    SLOT 2 VIOLATION TABLE — if any of these near-miss forms appear in your Contrast
    sentence, revert Slot 2 to blank template and rewrite:
    | Quoted near-miss form                                             | Violation type           |
    |-------------------------------------------------------------------|--------------------------|
    | "The [ns] namespace shows unlike evidence-heavy counterparts..."  | namespace-level subject   |
    | "Unlike other namespaces, coverage here is fully structural..."   | anonymous "coverage here" |
    | "This namespace's outputs differ from evidence-requiring types..."| artifact-level trigger    |
    Token match: if your Contrast sentence contains "namespace shows", "coverage here", or
    "This namespace's outputs", it matches a table row.
    HALT. Delete the violating line. Rewrite in PASS form.

  Structural position (SLOT 1 — second to write, after Contrast is complete):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  CONSTRAINT: Slot 1 Structural position MUST name the SQ-1 decision verbatim.
  If the written Slot 1 is a generic adequacy statement without the SQ-1 decision name:
    HALT. Delete the violating line. Rewrite in PASS form.

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
  Section Coverage: Coverage Review table — | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Section Structural records (one line per namespace, artifact-as-subject form):
    "The mock artifact's [ns] section records / lacks [specific structural element]."

  Section Risk:
    For each REAL-REQUIRED: "[ns] URGENCY:[BLOCKING | HIGH | MEDIUM] — {decision at risk}"
    Cross-namespace: "Highest-risk gap: {namespace} — {Tier {tier} decision} — urgency: {level}"

  Section Next Steps: numbered list, one entry per REAL-REQUIRED namespace.
    Format: "/{skill-id} {topic} — {Artifact state}"

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
    Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  [BRANCH A output OR BRANCH B output — exactly one, never both]

---

STEP 9 — GATE F: COMPLETENESS GATE (named step, not optional)

Before reporting done, verify all review artifact sections are complete by stable section ID:

  GATE F — Section-by-section check:
  - Section Coverage: [present — {N} namespace rows | INCOMPLETE — {detail}]
  - Section Structural records: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Risk: [present — {N} entries | INCOMPLETE — {detail}]
  - Section Next Steps: [present — {N} entries | INCOMPLETE — {detail}]
  Total sections: {P} of 4 complete.
  Gate result: PASS (all 4 present) | FAIL ({section ID} incomplete)
  Do not proceed until written. If GATE F FAIL: return to failing section. Complete it. Recheck.
```

---

## Summary table

| V | Axis | C-23 form | C-24 form | C-25 form | Predicted ceiling |
|---|------|-----------|-----------|-----------|-------------------|
| V-01 | phrasing-register | HALT. Delete. Rewrite. in opening STANDING RULE | GATE F at STEP 8 end | prose note, no quoted forms | C-23 PASS; C-25 borderline |
| V-02 | output-format | borderline two-step (R4 form) | GATE F at STEP 8 end | SLOT 2 VIOLATION TABLE (3 quoted rows + token match) | C-25 PASS; C-23 borderline |
| V-03 | lifecycle-emphasis | HALT. Delete. Rewrite. co-located at each CONSTRAINT field | GATE F as named STEP 9 | prose note (held constant) | C-23 PASS via co-location; C-24 PASS at max; C-25 borderline |
| V-04 | phrasing-register + output-format | HALT. Delete. Rewrite. in opening STANDING RULE | GATE F as named STEP 9 | SLOT 2 VIOLATION TABLE (3 quoted rows) | C-23 PASS; C-24 PASS; C-25 PASS — predicted 17/17 |
| V-05 | all three axes | HALT. Delete. Rewrite. in opening rule + co-located at CONSTRAINT sites | GATE F as named STEP 9 | SLOT 2 VIOLATION TABLE + HALT/DELETE/REWRITE in table revert | C-23/C-24/C-25 PASS at max strength — candidate golden |

**Scoring prediction vs v5 rubric:**

- V-01: 15/17 aspirational = (15/17)×10 = 8.8 + 60 + 30 = **98.8**
- V-02: 15/17 aspirational = (15/17)×10 = 8.8 + 60 + 30 = **98.8**
- V-03: 15/17 aspirational = (15/17)×10 = 8.8 + 60 + 30 = **98.8**
- V-04: 17/17 aspirational = 10.0 + 60 + 30 = **100.0**
- V-05: 17/17 aspirational = 10.0 + 60 + 30 = **100.0**

**Primary scoring test:** Does V-04 confirm 100? If V-04 < 100, the gap is either C-23 (opening rule location insufficient vs. co-location requirement) or C-25 (table structure insufficient vs. prose note). V-01/V-02 single-axis scores diagnose which.
