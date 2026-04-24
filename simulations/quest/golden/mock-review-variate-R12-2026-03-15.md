---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 12
rubric_version: v12
status: VARIATE
---

# mock-review Variate — Round 12

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v12 (C-01 through C-35; aspirational denominator = 27)
**Round:** R12 — targeting v12 new criteria: C-34, C-35

---

## What R11 Left Open

R11 V-05 (the ceiling) achieved C-32 (VERDICT-ECHO classification label inside the
`SQ answer driving verdict` field definition) and C-33 (next-steps REQUIRED-SLOT
declaration with named error TRACEABILITY-BREAK in the entry format). All R10 V-05 criteria
were preserved. Two residual gaps drive C-34/C-35, derived by the same logic C-32 used
over C-21 and C-33 used over C-24:

| Criterion | R11 ceiling coverage | Gap |
|-----------|---------------------|-----|
| C-33 → C-34 | R11 V-05 declares TRACEABILITY-BREAK as a named error in the next-steps REQUIRED SLOT declaration block. An entry missing the `{Artifact state}` third component is named as TRACEABILITY-BREAK. But the classification is in a surrounding declaration block — not embedded inside the entry format template itself. The entry format line reads `/{skill-id} {topic} — {Artifact state}` with REQUIRED SLOT label and TRACEABILITY-BREAK named in the surrounding text. C-34 requires the error label and classification test to appear inside the entry format template definition — classifiable at the template site without reading the surrounding declaration. Same gap as C-21→C-32: concept named in preamble, mechanical encoding absent in the field definition itself. | C-34 deepens C-33: the entry format template must carry an embedded ERROR — TRACEABILITY-BREAK classification block (analogous to ERROR — VERDICT ECHO in the SQ answer field) with a component-count rule, so violations are classifiable at the entry site from the template definition alone. A surrounding REQUIRED SLOT declaration that names TRACEABILITY-BREAK satisfies C-33 but not C-34, because the classification test is advisory (in surrounding text) rather than mechanical (in the template field definition). |
| C-26 partial → C-35 | R11 V-05 uses Architect-first ordering with a named cross-step guard (CONTRADICTS-ARCHITECTURE → block PM). C-26 is fully satisfied. But C-26 requires Architect-first ordering — in any design where Strategy runs before PM (especially non-Architect-first designs like Strategy→PM→Arch), no analogous guard for the Strategy verdict protects PM evaluation. R11 V-01 and V-02 both used Strategy-first orderings where C-26 was "structurally unreachable for this axis" — phase-level contamination existed but no named cross-step guard fired on Strategy verdict. | C-35 deepens C-26 for non-Architect-first orderings: in designs where Strategy evaluation precedes PM evaluation (Strategy→PM→Arch, or Arch→Strat→PM), a named guard must fire on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and block PM Evaluation as the suppressed step. The guard must name both the specific verdict value and the specific blocked step. In a non-Architect-first ordering, this is the primary contamination control. A skill that separates Strategy and PM into sequential steps without naming this cross-step guard on the Strategy verdict does not satisfy C-35. |

Same derivation logic: concept present in evidence, mechanical encoding absent in the
structural position required → new criterion names the encoding.

- **C-34**: TRACEABILITY-BREAK classification test embedded in next-steps entry format (deepens C-33 the way C-32 deepened C-21)
- **C-35**: Strategy-to-PM cross-step contamination guard naming `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and PM Evaluation as the suppressed step (deepens C-26 for non-Architect-first orderings)

Denominator: 25 → 27.

---

## V-01 — Output Format (TRACEABILITY-BREAK classification test in entry format; C-34 axis)

**axis:** output-format
**hypothesis:** Embedding the TRACEABILITY-BREAK error label WITH a classification test
(component-count rule + tense/component test) INSIDE the evaluation-driven entry format
template in STEP 7 — not only in surrounding REQUIRED SLOT declaration text — satisfies C-34
independently of any Strategy-to-PM guard (C-35 FAIL). Base: R11 V-05 full Architect-first
design, all R11 V-05 criteria preserved. The TRACEABILITY-BREAK classification test in the
template definition must be usable at the entry site without cross-reference to the
surrounding REQUIRED SLOT declaration. Expected: C-34 PASS; C-35 FAIL (no Strategy-to-PM
guard); C-26 PASS (Architect-first preserved); C-32 PASS; C-33 PASS; all R10 V-05 criteria
preserved.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state — not a finding,
  not a judgment. MOCK-ACCEPTED is an earned outcome that requires an argument against
  the default. A namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Absence of disqualification
  is not positive evidence. The inertia structure forces a genuine contrastive argument —
  confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design enables independent satisfaction of C-26 (role ordering) and
  C-27 (enumerable triad): the triad is verified here, at the gate, before any role
  step runs — making it independent of which role runs first.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation (Architect, Strategy, or PM) to any auto-flagged namespace is the
  named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.
  Any evaluation verdict applied to an auto-flagged namespace is void and must be discarded.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Architect Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — a yes/no answer does not satisfy.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Architect to PM (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Strategy Evaluation (STEP 4) may still run for all namespaces — coverage gap synthesis.
  Record the cross-step guard lists:
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation (architect-verdict = CONSISTENT-WITH-ARCHITECTURE): [{list}]

  This guard fires on the specific verdict value `architect-verdict = CONTRADICTS-ARCHITECTURE`
  and blocks the specific downstream step PM Evaluation (STEP 5). It is distinct from the
  AUTO-RULE CONTAMINATION GUARD at the PHASE GATE — that guard blocks evaluation of
  auto-flagged namespaces; this guard fires on a verdict value within the evaluation phase.
  DO NOT conflate the two guards.

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including cross-step-blocked — for coverage gap synthesis),
answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts are written for every
remaining namespace.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Namespaces on the cross-step-blocked list DO NOT proceed
to PM evaluation — their decision is already determined. Applying PM evaluation to a
cross-step-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: The `trigger` field is a named artifact field at fixed position.
  Second line of every REAL-REQUIRED block; third line of every MOCK-ACCEPTED block.
  Values from this enumeration only (lowercase, equals-sign notation):
    Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
    MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject, observable
state as object. Verdict echo is the named error VERDICT-ECHO — detectable when grammatical
subject is a role name or evaluation noun rather than an artifact name.
  Correct: "Section 3.2 lists no fallback path for this namespace."
  Verdict echo (named error): "Architect found no fallback path."

SQ-answer citation form: The sub-question answer field names a specific artifact in
present-tense artifact-state form. It is structurally distinguished from a verdict restatement
by having the artifact as subject, not the role. "Section 4.1 contains no tier-boundary gate"
is an SQ answer. "Architect found no gate" is a verdict echo. This distinction is a structural
rule — the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. A generic adequacy
          statement without this SQ-1 citation = SLOT VIOLATION. Example of SLOT VIOLATION:
          "this namespace has limited scope." Example of valid field: "Tier 1 scope gate:
          whether {topic} requires trace-level signal before proceeding."]
        Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
          required) or TIER-GATING (real evidence required; decision depends on live system
          state at tier boundaries). The slot requires the SQ-1 decision citation AND the
          type classification. Generic adequacy without both = SLOT VIOLATION.
  (2) Contrast: [Name a namespace type that WOULD require real evidence and state the
        structural factor it has that this namespace does not. Must name BOTH a namespace
        type AND the distinguishing structural factor. Form: "Unlike {namespace type}, which
        carries {structural factor} that requires real evidence because {reason}, this
        namespace's outputs are fully determined by {structural form property}."]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject. Observable
      state as predicate. Name the specific artifact, section, or element whose observed
      state drove the failing evaluation.
      Example valid: "Section 4.1 contains no tier-boundary gate."]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation. Example
      VERDICT ECHO: "Architect found no tier-boundary gate." — role as subject = VERDICT ECHO.
      Tense and subject together distinguish the forms: past-tense assessment with role as
      subject = VERDICT ECHO (void; rewrite required). Present-tense observable state with
      artifact as subject = valid SQ citation. Classifiable at the field site from this
      template definition alone — no cross-reference to prior sections required.
  Artifact state: [Present-tense artifact-state — artifact as subject]

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
    One row per namespace; all namespaces from the PHASE GATE partition and STEP 6.

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). An evaluation-driven next-steps entry that
      names only skill-id and topic without the `{Artifact state}` third component is:
        ERROR — TRACEABILITY-BREAK [classification label]
        Classification test: if the entry structure is `/{skill-id} {topic}` with no
          em-dash third component, it is a TRACEABILITY-BREAK — classifiable at this
          template site from this definition alone, without reading the surrounding
          REQUIRED SLOT declaration.
        Component-count rule: a valid evaluation-driven entry has EXACTLY 3 components:
          skill-id, topic, Artifact state. An entry with 2 components (skill-id + topic
          only) is a TRACEABILITY-BREAK regardless of content length or explanatory
          detail in the first two components.
        Tense/component test (parallel to VERDICT-ECHO in STEP 6): the third component
          uses present-tense artifact-state form with artifact as grammatical subject. A
          third component in past-tense with a role as subject is a VERDICT-ECHO-IN-NEXT-STEPS
          — a distinct error from TRACEABILITY-BREAK but equally void. Two named error
          classes at this template site:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense (e.g., "Architect found no gate" rather than "Section 4.1 has no gate").
          Neither is a valid entry; both require rewrite before this section is complete.
        This classification is deterministic from entry structure — no content judgment
          required. Breaking the end-to-end chain (SQ answer → Artifact state field →
          next-steps entry) at the final link is the TRACEABILITY-BREAK error.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}
      An auto-flagged entry that omits the trigger value is a traceability break.

  Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    Same entry formats and REQUIRED SLOTS / TRACEABILITY-BREAK classification as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. It is not optional.

Edit {mock-artifact-path} in-place using Edit tool. In-place replacement only.
Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

After completing all edits, verify before confirming.

Canary Confirmation — output protocol:
  The following line is a CANARY OUTPUT:
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion that the stated condition is true. Writing this line when any
  Status field remains as MOCK (awaiting review) is the named error CANARY-FALSE-POSITIVE.
  This error is not recoverable — the canary's value is that its presence asserts the
  condition is met; a false-positive canary destroys the assertion's meaning.

  Protocol:
    — Write the canary ONLY after confirming zero Status fields remain as MOCK.
    — If any Status field was not updated: suppress the canary. Output instead:
        "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
      Attempt remaining edits. Re-verify. Write canary only when condition is met.
    — DO NOT write the canary confirmation if the stated condition is not verified.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-02 — Role Sequence (Strategy-first ordering with C-35 cross-step guard; C-35 axis)

**axis:** role-sequence
**hypothesis:** Strategy-first ordering (Strategy → PM → Architect) with a named
cross-step guard that fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and
blocks PM Evaluation as the suppressed step satisfies C-35 independently of C-34 (no
TRACEABILITY-BREAK classification test in entry format). C-26 is structurally unreachable
in this design: Architect runs after PM, so the Architect-before-PM requirement is unmet.
C-32 (VERDICT-ECHO classification label inside SQ field) and C-33 (REQUIRED SLOT
declaration) are preserved from R11 V-05. Expected: C-35 PASS; C-34 FAIL (no embedded
classification test in entry template); C-26 FAIL (Strategy-first ordering puts Architect
after PM); C-32 PASS; C-33 PASS; all other R11 criteria preserved.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state — not a finding,
  not a judgment. MOCK-ACCEPTED is an earned outcome that requires an argument against
  the default. A namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Absence of disqualification
  is not positive evidence. The inertia structure forces a genuine contrastive argument —
  confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design is independent of role sequence: the triad is verified here
  at the gate before any role step runs.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation (Architect, Strategy, or PM) to any auto-flagged namespace is the
  named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.
  Any evaluation verdict applied to an auto-flagged namespace is void and must be discarded.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Strategy Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Strategy to PM (C-35 guard for non-Architect-first orderings):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 4) to these namespaces.
  This guard fires on the specific verdict value `strategy-verdict = INSUFFICIENT FOR
  TIER {tier}` and names PM Evaluation (STEP 4) as the suppressed step. In this
  Strategy-first ordering, Architect evaluation does not precede PM evaluation — this
  Strategy-to-PM guard is therefore the primary contamination control for PM evaluation
  quality. It prevents PM from certifying structural completeness of a namespace whose
  coverage adequacy is already determined to be insufficient for the tier.
  In a non-Architect-first ordering such as this one, there is no Architect-to-PM guard
  (C-26 guard) to protect the PM boundary from architecture-level contamination —
  Architect runs after PM. The Strategy-to-PM guard addresses coverage-adequacy
  contamination; architecture contamination from Architect is handled in STEP 5 as a
  post-PM correction.
  DO NOT conflate this Strategy-to-PM guard (fires on strategy-verdict = INSUFFICIENT
  FOR TIER {tier}) with a hypothetical Architect-to-PM guard (fires on
  architect-verdict = CONTRADICTS-ARCHITECTURE): they are distinct guards protecting
  the PM boundary from different contamination sources. Only the Strategy-to-PM guard
  applies in this ordering.
  Record:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation (strategy-verdict = ADEQUATE): [{list}]

DO NOT proceed to STEP 4 (PM Evaluation) until Strategy verdicts and cross-step guard
assignments are complete for all remaining namespaces.

---

STEP 4 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces where strategy-verdict = ADEQUATE FOR
TIER {tier}. Namespaces on the Strategy-blocked list DO NOT proceed to PM evaluation — their
preliminary decision is already REAL-REQUIRED. Applying PM evaluation to a Strategy-blocked
namespace is the named error STRATEGY-GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 5 (Architect Evaluation) until PM verdicts are written for every
qualifying namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including Strategy-blocked — for architecture review and
final decision resolution), answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

For namespaces where architect-verdict = CONTRADICTS-ARCHITECTURE: preliminary decision
is REAL-REQUIRED with trigger = ARCH-IMPLAUSIBLE, regardless of prior PM verdict.

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until Architect verdicts are written.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: The `trigger` field is a named artifact field at fixed position.
  Second line of every REAL-REQUIRED block; third line of every MOCK-ACCEPTED block.
  Values from this enumeration only (lowercase, equals-sign notation):
    Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
    MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject, observable
state as object. Verdict echo is the named error VERDICT-ECHO.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (named error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. Generic adequacy
          without this citation = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM or TIER-GATING.
  (2) Contrast: [Name a namespace type that WOULD require real evidence and state the
        structural factor it has that this namespace does not. Must name BOTH a namespace
        type AND the distinguishing structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject.]
    ERROR — VERDICT ECHO [classification label]: A field where the grammatical subject
      is a role name or evaluation noun. Classification test: role-as-subject = VERDICT ECHO.
      Classifiable at this field site from this template definition alone.
  Artifact state: [Present-tense artifact-state — artifact as subject]

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

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). An evaluation-driven next-steps entry that
      names only skill-id and topic without the `{Artifact state}` slot is the named error
      TRACEABILITY-BREAK. A TRACEABILITY-BREAK entry is structurally incomplete — it breaks
      the end-to-end traceability chain and must be corrected before the review artifact
      is complete.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical REAL-REQUIRED:
    Same entry formats and REQUIRED SLOTS declaration as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED:
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation — output protocol:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion. Writing it when any Status field remains MOCK is
  the named error CANARY-FALSE-POSITIVE. DO NOT write it unless condition is verified.
  If any field was not updated: suppress the canary; output:
    "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
  Attempt remaining edits. Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Role Sequence boundary (Architect-first + Strategy-to-PM guard without non-Architect-first framing; C-35 boundary test)

**axis:** role-sequence
**hypothesis:** In an Architect-first ordering (Arch → Strat → PM), adding a Strategy-to-PM
cross-step guard that fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names
PM Evaluation as the suppressed step partially satisfies C-35. The boundary question: does
C-35 require (a) the guard to exist in any ordering where Strategy precedes PM, or (b) the
guard text to explicitly acknowledge its role in non-Architect-first contexts? This variation
includes the guard mechanics without the non-Architect-first framing clause, testing whether
the framing clause is required for C-35. Expected: C-35 PARTIAL (guard mechanics present,
non-Architect-first framing absent); C-26 PASS (Architect-first preserved, with Arch-to-PM
guard); C-34 FAIL (no TRACEABILITY-BREAK classification test in entry template); C-32 PASS;
C-33 PASS.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned outcome that requires
  an argument against the default. A namespace earns MOCK-ACCEPTED only when all three role
  evaluations actively confirm it positively demonstrates what is required. Absence of
  disqualification is not positive evidence. The inertia structure forces a genuine
  contrastive argument.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design enables independent satisfaction of C-26 (role ordering) and
  C-27 (enumerable triad): verified here at the gate, independent of which role runs first.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. The automatic decision stands unconditionally.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Architect Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — yes/no answers do not satisfy.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Architect to PM (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Strategy Evaluation (STEP 4) may still run for all namespaces.
  Record:
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation (architect-verdict = CONSISTENT-WITH-ARCHITECTURE): [{list}]

  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and blocks
  PM Evaluation (STEP 5). Distinct from the AUTO-RULE CONTAMINATION GUARD — that guard
  blocks evaluation of auto-flagged namespaces; this guard fires on a verdict value.

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and blocks
  PM Evaluation (STEP 5). A namespace that clears the Architect guard (STEP 3) but
  receives strategy-verdict = INSUFFICIENT does not proceed to PM evaluation.
  Record:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT): [{list}]
    Proceeding to PM Evaluation (strategy-verdict = ADEQUATE): [{list}]
    Combined PM-blocked list (Architect-blocked + Strategy-blocked): [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
are complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where BOTH:
  architect-verdict = CONSISTENT-WITH-ARCHITECTURE
  strategy-verdict = ADEQUATE FOR TIER {tier}
A namespace blocked by either cross-step guard does not proceed to PM evaluation.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` field at fixed position in every decision block.
Values from enumeration only (lowercase, equals-sign notation):
  Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as subject. Role-as-subject =
named error VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  RATIONALE TEMPLATE (2 required slots — both required):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Strategy SQ-1 answer verbatim]
        Classify: STRUCTURAL-FORM or TIER-GATING
  (2) Contrast: [Namespace type that WOULD require real evidence + distinguishing structural factor]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state. Artifact as grammatical subject.]
    ERROR — VERDICT ECHO [classification label]: grammatical subject is a role name or
      evaluation noun. Classification test: role-as-subject = VERDICT ECHO. Classifiable
      at this field site from template definition alone.
  Artifact state: [Present-tense artifact-state — artifact as subject]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; ordering rule: "Critical namespaces first
  (trace, scout-feasibility, listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block. An entry without the `{Artifact state}` third component is the
      named error TRACEABILITY-BREAK. Correct before this section is complete.
    Auto-flagged: /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical REAL-REQUIRED: same formats as Priority 1.
  Priority 3 — Evidence-heavy: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {Tier {tier} decision at risk} — urgency: {level}"

DO NOT proceed to STEP 8 until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation:
  Write "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." ONLY after
  verifying zero Status fields remain as MOCK. Writing when any remain = named error
  CANARY-FALSE-POSITIVE. If fields remain: suppress canary, output:
    "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — Combined Role Sequence + Output Format (Strategy-first + C-34 classification test; C-34 + C-35 combined, C-26 boundary)

**axis:** role-sequence + output-format
**hypothesis:** Strategy-first ordering (Strategy → PM → Architect) with (1) C-35 cross-step
guard after Strategy and (2) TRACEABILITY-BREAK classification test embedded in the entry
format template satisfies both C-34 and C-35 in a single design. C-26 is structurally
unreachable (Architect after PM). All other R11 V-05 criteria preserved. Expected: C-34
PASS; C-35 PASS (Strategy-first + named guard with non-Architect-first framing); C-26 FAIL
(Architect not before PM); C-32 PASS; C-33 PASS; inertia framing (C-22) preserved.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state — not a finding,
  not a judgment. MOCK-ACCEPTED is an earned outcome that requires an argument against
  the default. A namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Absence of disqualification
  is not positive evidence. The inertia structure forces a genuine contrastive argument —
  confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  Co-location at gate is independent of role sequence: triad verified here before any
  role step runs.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Strategy Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Strategy to PM (C-35 guard for non-Architect-first orderings):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 4) to these namespaces.
  This guard fires on the specific verdict value `strategy-verdict = INSUFFICIENT FOR
  TIER {tier}` and names PM Evaluation (STEP 4) as the suppressed step. In this
  Strategy-first ordering, Architect evaluation does not precede PM evaluation —
  this Strategy-to-PM guard is the primary contamination control for PM evaluation
  quality in this non-Architect-first design. It prevents PM from certifying structural
  completeness of a namespace whose coverage adequacy is already determined to be
  insufficient for the tier.
  DO NOT conflate this Strategy-to-PM guard (fires on strategy-verdict = INSUFFICIENT
  FOR TIER {tier}, blocks STEP 4) with a hypothetical Architect-to-PM guard (fires on
  architect-verdict = CONTRADICTS-ARCHITECTURE, blocks PM): they are distinct guards
  protecting the PM boundary from different contamination sources.
  Record:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT): [{list}]
    Proceeding to PM Evaluation (strategy-verdict = ADEQUATE): [{list}]

DO NOT proceed to STEP 4 (PM Evaluation) until Strategy verdicts and cross-step guard
assignments are complete for all remaining namespaces.

---

STEP 4 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces where strategy-verdict = ADEQUATE FOR
TIER {tier}. Strategy-blocked namespaces DO NOT proceed to PM evaluation.
Applying PM evaluation to a Strategy-blocked namespace is the named error
STRATEGY-GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 5 (Architect Evaluation) until PM verdicts are written.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including Strategy-blocked — for architecture review),
answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" grammar — yes/no not sufficient.

  SQ-1: Name the system component, dependency, or interface that confirms plausibility
        (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact that most directly confirms or challenges
        this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

For namespaces where architect-verdict = CONTRADICTS-ARCHITECTURE: preliminary decision
is REAL-REQUIRED with trigger = ARCH-IMPLAUSIBLE, regardless of prior PM or Strategy verdict.

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` field at fixed position in every decision block.
  Values from enumeration only (lowercase, equals-sign notation):
    Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
    MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (named error VERDICT-ECHO): "Architect found no fallback path."

SQ-answer citation form: artifact as subject, present-tense. Role-as-subject = VERDICT-ECHO.
Classifiable at the field site from the template definition alone.

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  RATIONALE TEMPLATE (2 required slots — both must be populated):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Strategy SQ-1 answer verbatim. Generic adequacy = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM or TIER-GATING.
  (2) Contrast: [Namespace type that WOULD require real evidence + distinguishing structural
        factor it has that this namespace does not. Name BOTH.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense. Artifact as grammatical subject. Name the specific artifact,
      section, or element whose observed state drove the failing evaluation.]
    ERROR — VERDICT ECHO [classification label]: grammatical subject is a role name or
      evaluation noun. Classification test: role-as-subject = VERDICT ECHO. Classifiable
      at this field site from this template definition alone.
  Artifact state: [Present-tense artifact-state — artifact as subject]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |
    One row per namespace.

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). The end-to-end traceability chain is:
      SQ answer driving verdict → Artifact state field → this next-steps entry. Breaking
      the chain at the final link is:
        ERROR — TRACEABILITY-BREAK [classification label]
        Classification test: if the entry structure is `/{skill-id} {topic}` with no
          em-dash third component, it is a TRACEABILITY-BREAK — classifiable at this
          template site from this definition alone, without reading surrounding text.
        Component-count rule: valid evaluation-driven entry = EXACTLY 3 components
          (skill-id, topic, Artifact state). Entry with 2 components = TRACEABILITY-BREAK
          regardless of content length in the first two.
        Tense/component test (parallel to VERDICT-ECHO in STEP 6): the third component
          uses present-tense artifact-state form with artifact as grammatical subject.
          A third component with role as subject or in past-tense is a
          VERDICT-ECHO-IN-NEXT-STEPS — distinct from TRACEABILITY-BREAK but equally void.
          Error taxonomy at this template site:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: third component is role-subject, past-tense.
          Both require rewrite. Classification from entry structure — no content judgment.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}
      An auto-flagged entry that omits the trigger value is a traceability break.

  Priority 2 — Non-critical REAL-REQUIRED:
    Same entry formats, TRACEABILITY-BREAK classification, and error taxonomy as Priority 1.

  Priority 3 — Evidence-heavy:
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation — output protocol:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion. Writing it when any Status field remains MOCK is
  the named error CANARY-FALSE-POSITIVE. DO NOT write it unless condition is verified.
  If any field was not updated: suppress canary; output:
    "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
  Attempt remaining edits. Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — Full Integration (C-34 + C-35 + C-26 dual guard design; Arch → Strat → PM)

**axis:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** Architect → Strategy → PM ordering with (1) C-26 Architect-to-PM guard
(CONTRADICTS-ARCHITECTURE blocks PM, Architect before PM), (2) C-35 Strategy-to-PM guard
(INSUFFICIENT FOR TIER blocks PM, Strategy before PM, with explicit non-Architect-first
context framing: "in a non-Architect-first ordering, this guard is the primary contamination
control"), and (3) TRACEABILITY-BREAK classification test embedded in entry format (C-34)
achieves the full v12 criterion set. C-26 is satisfied because Architect runs before PM.
C-35 is satisfied because: (a) the Strategy-to-PM guard fires on the specific verdict value
`strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM Evaluation as the suppressed
step, (b) the guard text explicitly names its role in non-Architect-first contexts, making
it a named guard that applies whenever Strategy precedes PM — not only in Architect-first
designs. C-34 is satisfied because the TRACEABILITY-BREAK error label and component-count
classification test appear inside the entry format template definition in STEP 7, not only
in surrounding REQUIRED SLOT declaration text. All R11 V-05 criteria preserved: DEFAULT
DECISION POSITION block (C-22); PHASE GATE with co-located TRIAD "(3 rules, all required)"
(C-29, C-31); named DO NOT per rule (C-27); step-name anchors in all inter-step gates (C-28);
AUTO-RULE CONTAMINATION GUARD (C-17); entity-naming SQ grammar (C-15); VERDICT-ECHO
classification label inside SQ answer field (C-32); REQUIRED SLOT declaration with
TRACEABILITY-BREAK in next-steps (C-33); SQ-1 citation sub-field in MOCK-ACCEPTED Structural
position slot (C-30); RATIONALE TEMPLATE 2-slot structure with Contrast sub-slot (C-25);
canary false-positive prohibition (C-16); all other essential and recommended criteria.
Expected: C-34 PASS; C-35 PASS; C-26 PASS; C-25 PASS; C-28 PASS; C-29 PASS; C-31 PASS;
C-32 PASS; C-33 PASS; all prior criteria preserved. Full v12 criterion set satisfied.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state — not a finding,
  not a judgment. MOCK-ACCEPTED is an earned outcome that requires an argument against
  the default. A namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Absence of disqualification
  is not positive evidence. The inertia structure forces a genuine contrastive argument —
  confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design enables independent satisfaction of C-26 (Architect-to-PM guard
  in role ordering) and C-27 (enumerable triad): the triad is verified here, at the gate,
  before any role step runs — making it independent of which role runs first.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation (Architect, Strategy, or PM) to any auto-flagged namespace is the
  named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.
  Any evaluation verdict applied to an auto-flagged namespace is void and must be discarded.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Architect Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — a yes/no answer does not satisfy.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Architect to PM (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Strategy Evaluation (STEP 4) may still run for all namespaces — coverage gap synthesis.
  Record the cross-step guard lists:
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy and PM (architect-verdict = CONSISTENT-WITH-ARCHITECTURE): [{list}]

  This guard fires on the specific verdict value `architect-verdict = CONTRADICTS-ARCHITECTURE`
  and blocks the specific downstream step PM Evaluation (STEP 5). It is distinct from the
  AUTO-RULE CONTAMINATION GUARD at the PHASE GATE — that guard blocks evaluation of
  auto-flagged namespaces; this guard fires on a verdict value within the evaluation phase.
  DO NOT conflate the two guards.

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including Architect-blocked — for coverage gap synthesis),
answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Strategy to PM (C-35 guard for non-Architect-first orderings):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on the specific verdict value `strategy-verdict = INSUFFICIENT FOR
  TIER {tier}` and names PM Evaluation (STEP 5) as the suppressed step. In a
  non-Architect-first ordering (e.g., Strategy → PM → Architect), this Strategy-to-PM
  guard is the primary contamination control for PM evaluation quality — there is no
  Architect-to-PM guard (C-26) to protect the PM boundary, so the Strategy verdict
  becomes the first line of defense. Even in this Architect-first design, the guard
  provides a second layer of PM boundary protection: a namespace that clears
  Architect evaluation but whose coverage is determined inadequate for the tier is
  stopped before PM certifies structural completeness on an already-inadequate coverage
  foundation.
  DO NOT conflate this Strategy-to-PM guard (fires on strategy-verdict = INSUFFICIENT
  FOR TIER {tier}, blocks STEP 5 PM Evaluation) with the Architect-to-PM guard (C-26,
  fires on architect-verdict = CONTRADICTS-ARCHITECTURE, also blocks STEP 5 PM
  Evaluation): they are distinct guards protecting the PM boundary from different
  contamination sources — architecture quality and coverage adequacy respectively.
  Two separate guards protect STEP 5; a namespace must clear both to proceed to PM.
  Record:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT): [{list}]
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE,
      from STEP 3): [{list — repeat for completeness}]
    Combined PM-blocked list: [{union of both guard lists}]
    Proceeding to PM Evaluation (cleared both guards): [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and cross-step guard
assignments are complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces that have cleared BOTH cross-step guards:
  architect-verdict = CONSISTENT-WITH-ARCHITECTURE (C-26 guard cleared)
  strategy-verdict = ADEQUATE FOR TIER {tier} (C-35 guard cleared)
A namespace blocked by either guard does not proceed to PM evaluation. Applying PM
evaluation to any guard-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: The `trigger` field is a named artifact field at fixed position.
  Second line of every REAL-REQUIRED block; third line of every MOCK-ACCEPTED block.
  Values from this enumeration only (lowercase, equals-sign notation):
    Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
    MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject, observable
state as object. Verdict echo is the named error VERDICT-ECHO — detectable when grammatical
subject is a role name or evaluation noun rather than an artifact name.
  Correct: "Section 3.2 lists no fallback path for this namespace."
  Verdict echo (named error): "Architect found no fallback path."

SQ-answer citation form: The sub-question answer field names a specific artifact in
present-tense artifact-state form. It is structurally distinguished from a verdict restatement
by having the artifact as subject, not the role. "Section 4.1 contains no tier-boundary gate"
is an SQ answer. "Architect found no gate" is a verdict echo. This distinction is a structural
rule — the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. A generic adequacy
          statement without this SQ-1 citation = SLOT VIOLATION. Example of SLOT VIOLATION:
          "this namespace has limited scope." Example of valid field: "Tier 1 scope gate:
          whether {topic} requires trace-level signal before proceeding."]
        Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
          required) or TIER-GATING (real evidence required; decision depends on live system
          state at tier boundaries). The slot requires the SQ-1 decision citation AND the
          type classification. Generic adequacy without both = SLOT VIOLATION.
  (2) Contrast: [Name a namespace type that WOULD require real evidence and state the
        structural factor it has that this namespace does not. Must name BOTH a namespace
        type AND the distinguishing structural factor. Form: "Unlike {namespace type}, which
        carries {structural factor} that requires real evidence because {reason}, this
        namespace's outputs are fully determined by {structural form property}."]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject. Observable
      state as predicate. Name the specific artifact, section, or element whose observed
      state drove the failing evaluation.
      Example valid: "Section 4.1 contains no tier-boundary gate."]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation. Example
      VERDICT ECHO: "Architect found no tier-boundary gate." — role as subject = VERDICT ECHO.
      Tense and subject together distinguish the forms: past-tense assessment with role as
      subject = VERDICT ECHO (void; rewrite required). Present-tense observable state with
      artifact as subject = valid SQ citation. Classifiable at the field site from this
      template definition alone — no cross-reference to prior sections required.
  Artifact state: [Present-tense artifact-state — artifact as subject]

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
    One row per namespace; all namespaces from the PHASE GATE partition and STEP 6.

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). This slot closes the end-to-end traceability
      chain: SQ answer driving verdict → Artifact state field → this next-steps entry.
      Breaking the chain at the final link is:
        ERROR — TRACEABILITY-BREAK [classification label]
        Classification test: if the entry structure is `/{skill-id} {topic}` with no
          em-dash third component, it is a TRACEABILITY-BREAK — classifiable at this
          template site from this definition alone, without reading the surrounding
          REQUIRED SLOT declaration.
        Component-count rule: a valid evaluation-driven entry has EXACTLY 3 components:
          skill-id, topic, Artifact state. An entry with 2 components (skill-id + topic
          only) is a TRACEABILITY-BREAK regardless of content length or explanatory
          detail in the first two components.
        Tense/component test (parallel to VERDICT-ECHO in STEP 6 SQ field): the third
          component uses present-tense artifact-state form with artifact as grammatical
          subject. A third component in past-tense with a role as subject is a
          VERDICT-ECHO-IN-NEXT-STEPS — a distinct named error from TRACEABILITY-BREAK
          but equally void.
        Error taxonomy at this template site (two named error classes):
          TRACEABILITY-BREAK: entry has 2 components (third slot absent entirely).
          VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
            past-tense form (e.g., "Architect found no gate" rather than "Section 4.1 has
            no gate"). Third slot is present but invalid.
        Both require rewrite before this next-steps section is complete. Classification
          is deterministic from entry structure — no content judgment required.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}
      An auto-flagged entry that omits the trigger value is a traceability break.

  Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    Same entry formats, TRACEABILITY-BREAK classification, and error taxonomy as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. It is not optional.

Edit {mock-artifact-path} in-place using Edit tool. In-place replacement only.
Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

After completing all edits, verify before confirming.

Canary Confirmation — output protocol:
  The following line is a CANARY OUTPUT:
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion that the stated condition is true. Writing this line when any
  Status field remains as MOCK (awaiting review) is the named error CANARY-FALSE-POSITIVE.
  This error is not recoverable — the canary's value is that its presence asserts the
  condition is met; a false-positive canary destroys the assertion's meaning.

  Protocol:
    — Write the canary ONLY after confirming zero Status fields remain as MOCK.
    — If any Status field was not updated: suppress the canary. Output instead:
        "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
      Attempt remaining edits. Re-verify. Write canary only when condition is met.
    — DO NOT write the canary confirmation if the stated condition is not verified.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
