Good — I now have the full R12 canonical baseline (V-01: Arch→Strat→PM, C-34 PASS / C-35 FAIL; V-02: Strat→PM→Arch, C-35 PASS / C-34 FAIL / C-26 FAIL). I have everything needed to derive the R13 variations.

Key derivation for R13:
- **C-36** = Strategy-to-PM guard required **in Arch-first** (Arch→Strat→PM) ordering. R12 V-01 lacked it → C-36 closes that gap.
- **C-37** = VERDICT-ECHO-IN-NEXT-STEPS **declared as parallel** to VERDICT-ECHO in the template definition itself. R12 V-01 has behavioral parallel but no symmetry declaration block.

---

## mock-review Variate — Round 13

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v13 (C-01 through C-37; aspirational denominator = 29)
**Round:** R13 — targeting v13 new criteria: C-36, C-37

---

### What R12 Left Open

| Criterion | R12 ceiling coverage | Gap |
|-----------|---------------------|-----|
| **C-35 FAIL (V-01, Arch-first)** | R12 V-01 uses Arch→Strat→PM. The C-26 Architect-to-PM guard is named and fires on `architect-verdict = CONTRADICTS-ARCHITECTURE`. Strategy runs at STEP 4, PM at STEP 5. No guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` before PM Evaluation in this Arch-first design. C-35 PASS was achieved only in V-02 (non-Arch-first Strategy-first ordering). | C-36: the Arch-first design has Strategy preceding PM (STEP 4 → STEP 5) but carries no Strategy-to-PM cross-step guard. The contamination vector exists in the canonical design — only the C-26 guard protects PM, and C-26 fires on architecture verdict, not coverage verdict. A Strategy result of INSUFFICIENT FOR TIER {tier} does not block PM in R12 V-01. C-36 closes this gap: the guard must be present in Arch-first ordering independently, named for the specific verdict value and the suppressed step. |
| **C-35 PASS (V-02) + C-34 FAIL (V-02)** | R12 V-02 names VERDICT-ECHO-IN-NEXT-STEPS in STEP 6 and includes the tense/component test as a "parallel to VERDICT-ECHO in STEP 6" note inside the entry format. The note is present and the behavioral parallel is described. But C-37 requires the symmetry to be DECLARED — a named structural block in the template definition that formally establishes the cross-template relationship between the two error classes. The "parallel to VERDICT-ECHO in STEP 6" note in R12 is a descriptive reference embedded in prose, not a dedicated symmetry declaration block at the template level. Declared symmetry and present symmetry are structurally distinct: declared symmetry appears as an explicit block in the template definition, making the relationship visible at the template site as a structural property. | C-37: the symmetry declaration must appear as a named block (e.g., CROSS-TEMPLATE ERROR SYMMETRY) in the entry format template definition — not only as a descriptive note inside a classification section. The block names VERDICT-ECHO-IN-NEXT-STEPS as the parallel error to VERDICT-ECHO, names the two template sites, and names the shared classification principle. A descriptive note satisfies behavioral parallel but not declared structural symmetry. |

Same derivation logic: concept present in evidence, structural declaration absent → C-36 names the Arch-first guard encoding, C-37 names the symmetry declaration block.

- **C-36**: Strategy-to-PM cross-step guard in Arch-first ordering — fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}`, names PM Evaluation (STEP 5) as the suppressed step. Required as an independent guard alongside C-26 in the canonical Arch→Strat→PM design.
- **C-37**: Cross-template error symmetry declaration — a named block in the STEP 7 entry format template that explicitly declares VERDICT-ECHO-IN-NEXT-STEPS as the parallel error to VERDICT-ECHO, names both template sites, and names the shared classification principle. The declaration must appear in the template definition itself, not in surrounding guidance or prose notes.

Denominator: 27 → 29.

---

## V-01 — Output Format: C-37 symmetry declaration in Arch-first base (C-37 axis)

**axis:** output-format
**hypothesis:** Adding a dedicated CROSS-TEMPLATE ERROR SYMMETRY declaration block to the STEP 7 entry format template in the Arch-first base independently satisfies C-37. The declaration is a named structural block — not a descriptive note — that explicitly states VERDICT-ECHO-IN-NEXT-STEPS is the parallel error to VERDICT-ECHO, names both template sites, and names the shared classification principle. C-36 is intentionally absent (single-axis test). All R12 V-01 criteria preserved.

**Expected:** C-37 PASS; C-36 FAIL (no Strategy-to-PM guard in Arch-first ordering); C-35 STRUCTURALLY UNREACHABLE (Arch-first design); C-26 PASS; C-34 PASS; C-33 PASS; C-32 PASS; all R12 V-01 criteria preserved.

---

```
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
        Tense/component test: the third component uses present-tense artifact-state form
          with artifact as grammatical subject. A third component in past-tense with a
          role as subject is a VERDICT-ECHO-IN-NEXT-STEPS error. Two named error classes:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense (e.g., "Architect found no gate" rather than "Section 4.1 has no gate").
          Neither is a valid entry; both require rewrite before this section is complete.
        This classification is deterministic from entry structure — no content judgment
          required. Breaking the end-to-end chain (SQ answer → Artifact state field →
          next-steps entry) at the final link is the TRACEABILITY-BREAK error.

    CROSS-TEMPLATE ERROR SYMMETRY DECLARATION:
      VERDICT-ECHO-IN-NEXT-STEPS is the parallel error to VERDICT-ECHO (STEP 6 SQ answer
      field). Both errors implement the same classification principle: a role or verdict
      used as grammatical subject produces a void content slot. The principle is applied
      at two distinct template sites:
        VERDICT-ECHO: applied at the SQ answer field in STEP 6. Classification test:
          if grammatical subject is a role label (Architect, PM, Strategy) → VERDICT-ECHO.
        VERDICT-ECHO-IN-NEXT-STEPS: applied at the {Artifact state} slot in this STEP 7
          entry format. Classification test: if the third component uses a role as subject
          in past tense → VERDICT-ECHO-IN-NEXT-STEPS.
      This symmetry is declared here, in the entry format template definition, making the
      cross-template relationship visible at this site without requiring cross-reference to
      STEP 6. The declaration is structural — not a prose note — and applies independently
      of which step is being evaluated.

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
```

---

## V-02 — Role Sequence: Strategy-first (Strat→Arch→PM) with C-35 guard; C-37 absent (C-35 axis re-test)

**axis:** role-sequence
**hypothesis:** Strategy-first ordering (Strat→Arch→PM) with the C-35 cross-step guard and a full C-34 TRACEABILITY-BREAK classification block preserves all R12 V-01 criteria that were achievable in this ordering. C-36 is structurally unreachable (C-36 requires Arch-first ordering; this is Strategy-first). C-37 is intentionally absent (single-axis test). C-26 is preserved: Arch runs at STEP 4 before PM at STEP 5.

**Expected:** C-35 PASS; C-26 PASS; C-34 PASS; C-33 PASS; C-36 STRUCTURALLY UNREACHABLE; C-37 FAIL; all achievable R12 criteria preserved.

---

```
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

CROSS-STEP GUARD — Strategy to PM (C-35: Strategy-first ordering Strategy-to-PM guard):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Architect Evaluation (STEP 4) may still run for architecture coverage synthesis.
  This guard fires on the specific verdict value `strategy-verdict = INSUFFICIENT FOR
  TIER {tier}` and names PM Evaluation (STEP 5) as the suppressed step. In this
  Strategy-first ordering, Strategy is the first contamination filter: a namespace
  with insufficient coverage adequacy cannot earn structural completeness credit from PM.
  This is the primary PM boundary guard in this ordering.
  Record:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Architect then PM Evaluation: [{list}]

DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including Strategy-blocked — for architecture coverage
synthesis and final determination), answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

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
  Record:
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation (CONSISTENT-WITH-ARCHITECTURE and not Strategy-blocked): [{list}]

  This guard fires on the specific verdict value `architect-verdict = CONTRADICTS-ARCHITECTURE`
  and blocks PM Evaluation (STEP 5). It is distinct from the Strategy-to-PM guard in STEP 3.
  Both guards protect the PM boundary from different contamination sources; both must be
  checked before PM Evaluation begins.
  DO NOT conflate the two guards.

DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and cross-step guard
assignments are complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where ALL of:
  — strategy-verdict = ADEQUATE FOR TIER {tier}
  — architect-verdict = CONSISTENT-WITH-ARCHITECTURE
Namespaces on either cross-step-blocked list DO NOT proceed to PM evaluation. Applying
PM evaluation to a cross-step-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

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
present-tense artifact-state form. Structurally distinguished from a verdict restatement
by having the artifact as subject, not the role. This distinction is a structural rule —
the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. A generic adequacy
          statement without this SQ-1 citation = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM or TIER-GATING. The slot requires both the SQ-1 decision
          citation AND the type classification. Generic adequacy without both = SLOT VIOLATION.
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
      state as predicate.]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation.
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
        Tense/component test: the third component uses present-tense artifact-state form
          with artifact as grammatical subject. A third component in past-tense with a
          role as subject is a VERDICT-ECHO-IN-NEXT-STEPS — a distinct error from
          TRACEABILITY-BREAK but equally void. Two named error classes at this template site:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense (e.g., "Architect found no gate" rather than "Section 4.1 has no gate").
          Neither is a valid entry; both require rewrite before this section is complete.
        This classification is deterministic from entry structure — no content judgment
          required.

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
```

---

## V-03 — Lifecycle Emphasis: C-36 guard in Arch-first ordering; C-37 absent (C-36 axis)

**axis:** lifecycle-emphasis
**hypothesis:** In the Arch-first base (Arch→Strat→PM), adding an explicit C-36 Strategy-to-PM cross-step guard at STEP 4 — with a named lifecycle gate block carrying both the trigger condition and the suppressed step label — independently satisfies C-36. The guard is structurally parallel to C-26 but fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` at the Strategy boundary rather than the Architect boundary. C-37 is intentionally absent (single-axis test). All R12 V-01 criteria preserved.

**Expected:** C-36 PASS; C-37 FAIL; C-35 STRUCTURALLY UNREACHABLE; C-26 PASS; C-34 PASS; all R12 V-01 criteria preserved.

---

```
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

CROSS-STEP GATE A — Architect to PM (C-26):
  ┌─────────────────────────────────────────────────────────────────────┐
  │ GATE A: Architect Boundary                                          │
  │ Trigger: architect-verdict = CONTRADICTS-ARCHITECTURE               │
  │ Action:  preliminary decision = REAL-REQUIRED; trigger = ARCH-IMPL. │
  │ Suppresses: PM Evaluation (STEP 5)                                  │
  │ DO NOT apply PM Evaluation (STEP 5) to namespaces at this gate.     │
  │ Strategy Evaluation (STEP 4) may still run — gap synthesis.         │
  └─────────────────────────────────────────────────────────────────────┘
  Record the cross-step guard lists:
    Blocked from PM Evaluation at Gate A
      (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding past Gate A: [{list}]

  GATE A is distinct from GATE B (below). DO NOT conflate.

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and Gate A
assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including Gate-A-blocked — for coverage gap synthesis),
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

CROSS-STEP GATE B — Strategy to PM (C-36: Arch-first ordering Strategy-to-PM guard):
  ┌─────────────────────────────────────────────────────────────────────┐
  │ GATE B: Strategy Boundary (Arch-first ordering)                     │
  │ Trigger: strategy-verdict = INSUFFICIENT FOR TIER {tier}            │
  │ Action:  preliminary decision = REAL-REQUIRED; trigger = STRAT-INAD.│
  │ Suppresses: PM Evaluation (STEP 5)                                  │
  │ DO NOT apply PM Evaluation (STEP 5) to namespaces at this gate.     │
  └─────────────────────────────────────────────────────────────────────┘
  This is the C-36 guard. In this Arch-first ordering (Arch→Strat→PM), Strategy runs at
  STEP 4 and PM at STEP 5 — Strategy precedes PM. Without GATE B, a namespace determined
  to have insufficient coverage adequacy for Tier {tier} would still receive PM structural
  completeness evaluation, creating a contamination path: PM could certify structural
  form for a namespace whose coverage inadequacy is already determined. GATE B closes this
  path. GATE B fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. This guard is independent of GATE A — they
  fire on different verdict values and protect PM from different contamination sources.
  DO NOT conflate GATE B (Strategy boundary) with GATE A (Architect boundary).
  Record:
    Blocked from PM Evaluation at Gate B
      (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation (clear of both Gate A and Gate B): [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and Gate B
assignments are complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces that cleared BOTH Gate A and Gate B:
  — architect-verdict = CONSISTENT-WITH-ARCHITECTURE (Gate A cleared)
  — strategy-verdict = ADEQUATE FOR TIER {tier} (Gate B cleared)
Namespaces on either blocked list DO NOT proceed to PM evaluation. Applying PM evaluation
to a gate-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

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
by having the artifact as subject, not the role. This distinction is a structural rule —
the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. A generic adequacy
          statement without this SQ-1 citation = SLOT VIOLATION. Example: "Tier 1 scope gate:
          whether {topic} requires trace-level signal before proceeding."]
        Classify: STRUCTURAL-FORM or TIER-GATING. Both SQ-1 citation and classification
          are required. Generic adequacy without both = SLOT VIOLATION.
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
      state as predicate.]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation.
      Tense and subject together distinguish the forms: past-tense assessment with role as
      subject = VERDICT ECHO (void; rewrite required). Present-tense observable state with
      artifact as subject = valid SQ citation. Classifiable at the field site from this
      template definition alone.
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
          template site from this definition alone.
        Component-count rule: a valid evaluation-driven entry has EXACTLY 3 components:
          skill-id, topic, Artifact state. An entry with 2 components is a TRACEABILITY-BREAK
          regardless of content length.
        Tense/component test: the third component uses present-tense artifact-state form
          with artifact as grammatical subject. A third component in past-tense with a role
          as subject is a VERDICT-ECHO-IN-NEXT-STEPS — a distinct error from TRACEABILITY-BREAK
          but equally void. Two named error classes:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense.
          Neither is a valid entry; both require rewrite.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}

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
  Writing this line when any Status field remains as MOCK is the named error CANARY-FALSE-POSITIVE.
  Protocol:
    — Write the canary ONLY after confirming zero Status fields remain as MOCK.
    — If any Status field was not updated: suppress the canary. Output:
        "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
      Attempt remaining edits. Re-verify. Write canary only when condition is met.
    — DO NOT write the canary if the stated condition is not verified.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-04 — Combined: Role Sequence (Strat→Arch→PM) + Phrasing Register (GATE notation throughout); C-35 + C-37

**axis:** role-sequence + phrasing-register
**hypothesis:** Strategy-first ordering (Strat→Arch→PM) using named GATE notation throughout (GATE A = Strat→PM, GATE B = Arch→PM) satisfies C-35 (the Strategy-to-PM guard fires in non-Arch-first ordering) and preserves C-26 (Arch precedes PM). Adding the C-37 CROSS-TEMPLATE ERROR SYMMETRY DECLARATION to STEP 7 satisfies C-37 in this role ordering. C-36 is structurally unreachable: C-36 requires Arch-first ordering; this is Strategy-first. The GATE notation register change from C-26's prose guard to named GATE blocks makes cross-step guards mechanically uniform — the same notation for both guards at both step boundaries.

**Expected:** C-35 PASS; C-26 PASS; C-37 PASS; C-36 STRUCTURALLY UNREACHABLE; C-34 PASS; C-33 PASS; C-32 PASS; all achievable R12 criteria preserved.

---

```
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
  Applying evaluation (Strategy, Architect, or PM) to any auto-flagged namespace is the
  named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.
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

┌─────────────────────────────────────────────────────────────────────────────┐
│ GATE A — Strategy to PM (C-35: non-Arch-first Strategy-to-PM guard)        │
│ Fires on:   strategy-verdict = INSUFFICIENT FOR TIER {tier}                 │
│ Action:     preliminary decision = REAL-REQUIRED; trigger = STRATEGY-INAD.  │
│ Suppresses: PM Evaluation (STEP 5)                                          │
│                                                                             │
│ DO NOT apply PM Evaluation (STEP 5) to namespaces where Gate A fires.      │
│ Architect Evaluation (STEP 4) proceeds for all namespaces — gap synthesis.  │
└─────────────────────────────────────────────────────────────────────────────┘
  GATE A fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and suppresses
  PM Evaluation (STEP 5). In this Strategy-first ordering, GATE A is the primary PM
  boundary guard for coverage adequacy. It is distinct from GATE B below (which
  guards the PM boundary from architecture-level contamination).
  DO NOT conflate GATE A (coverage adequacy boundary) with GATE B (plausibility boundary).
  Record:
    GATE A blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    GATE A clear (strategy-verdict = ADEQUATE): [{list}]

DO NOT proceed to STEP 4 (Architect Evaluation) until GATE A is applied to every namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace (including GATE A blocked — for architectural coverage
synthesis and final decision confirmation), answer sub-questions then write the
Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

┌─────────────────────────────────────────────────────────────────────────────┐
│ GATE B — Architect to PM (C-26: Architect-to-PM guard)                     │
│ Fires on:   architect-verdict = CONTRADICTS-ARCHITECTURE                    │
│ Action:     preliminary decision = REAL-REQUIRED; trigger = ARCH-IMPLAUS.   │
│ Suppresses: PM Evaluation (STEP 5)                                          │
│                                                                             │
│ DO NOT apply PM Evaluation (STEP 5) to namespaces where Gate B fires.      │
└─────────────────────────────────────────────────────────────────────────────┘
  GATE B fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and suppresses PM
  Evaluation (STEP 5). GATE B protects PM from architecture-level contamination.
  GATE B is distinct from GATE A (coverage adequacy boundary). Both gates must clear
  before a namespace reaches PM Evaluation.
  DO NOT conflate GATE B with GATE A.
  Record:
    GATE B blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    GATE B clear AND GATE A clear — proceed to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until GATE B is applied to every namespace.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces that cleared BOTH gates:
  — GATE A clear: strategy-verdict = ADEQUATE FOR TIER {tier}
  — GATE B clear: architect-verdict = CONSISTENT-WITH-ARCHITECTURE
Applying PM evaluation to a gate-blocked namespace is the named error GUARD-BYPASS
CONTAMINATION.

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
present-tense artifact-state form. Structurally distinguished by having the artifact as
subject, not the role. This distinction is a structural rule — the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim. Generic adequacy without this citation = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM or TIER-GATING. Both SQ-1 citation AND classification
          required. Generic adequacy without both = SLOT VIOLATION.
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
    Form: [Present-tense artifact-state form. Artifact as grammatical subject.]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label → VERDICT ECHO. Classifiable at the field site from this
      template definition alone.
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
          template site from this definition alone.
        Component-count rule: a valid evaluation-driven entry has EXACTLY 3 components:
          skill-id, topic, Artifact state. An entry with 2 components is TRACEABILITY-BREAK.
        Tense/component test: the third component uses present-tense artifact-state form
          with artifact as grammatical subject. Two named error classes at this template site:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense.
          Neither is a valid entry; both require rewrite.

    ╔═══════════════════════════════════════════════════════════════════════╗
    ║ CROSS-TEMPLATE ERROR SYMMETRY DECLARATION                           ║
    ║                                                                     ║
    ║ VERDICT-ECHO-IN-NEXT-STEPS is the parallel error to VERDICT-ECHO.  ║
    ║                                                                     ║
    ║ Both errors implement the same classification principle:             ║
    ║   a role or verdict used as grammatical subject produces a void     ║
    ║   content slot. The principle is applied at two template sites:     ║
    ║                                                                     ║
    ║   VERDICT-ECHO (STEP 6, SQ answer field):                           ║
    ║     Test: grammatical subject is a role label → VERDICT-ECHO.      ║
    ║     Site: `SQ answer driving verdict` field in REAL-REQUIRED block. ║
    ║                                                                     ║
    ║   VERDICT-ECHO-IN-NEXT-STEPS (STEP 7, {Artifact state} slot):      ║
    ║     Test: third component uses role as subject, past tense          ║
    ║           → VERDICT-ECHO-IN-NEXT-STEPS.                            ║
    ║     Site: `{Artifact state}` slot in this entry format.            ║
    ║                                                                     ║
    ║ This symmetry is a structural declaration in this template          ║
    ║ definition — visible at this template site without cross-reference  ║
    ║ to STEP 6.                                                          ║
    ╚═══════════════════════════════════════════════════════════════════════╝

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}

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
  Writing this line when any Status field remains as MOCK is the named error CANARY-FALSE-POSITIVE.
  Protocol:
    — Write the canary ONLY after confirming zero Status fields remain as MOCK.
    — If any Status field was not updated: suppress the canary. Output:
        "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
      Attempt remaining edits. Re-verify. Write canary only when condition is met.
    — DO NOT write the canary if the stated condition is not verified.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-05 — Golden Synthesis: Arch-first (Arch→Strat→PM) + C-36 guard + C-37 declaration

**axis:** lifecycle-emphasis + inertia-framing
**hypothesis:** The Arch-first canonical ordering (Arch→Strat→PM) with both the C-36 Strategy-to-PM guard (fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}`, suppresses STEP 5) and the C-37 CROSS-TEMPLATE ERROR SYMMETRY DECLARATION block in the STEP 7 entry format template satisfies all R13 criteria. C-26 (Arch→PM guard) and C-36 (Strat→PM guard in Arch-first ordering) are structurally independent guards in the same design, both protecting the PM boundary from distinct contamination sources. C-37 is a named structural block in the entry format definition — not a prose note — making the cross-template relationship mechanically visible at the entry site. C-35 is structurally unreachable: C-35 governs non-Arch-first orderings; this is the Arch-first canonical design. All R12 V-01 criteria preserved.

**Expected:** C-36 PASS; C-37 PASS; C-26 PASS; C-34 PASS; C-33 PASS; C-32 PASS; C-35 STRUCTURALLY UNREACHABLE; all 35 R12 criteria preserved.

---

```
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
    Proceeding to Strategy Evaluation and potentially PM: [{list}]

  This guard fires on the specific verdict value `architect-verdict = CONTRADICTS-ARCHITECTURE`
  and blocks the specific downstream step PM Evaluation (STEP 5). It is distinct from the
  AUTO-RULE CONTAMINATION GUARD at the PHASE GATE — that guard blocks evaluation of
  auto-flagged namespaces; this guard fires on a verdict value within the evaluation phase.
  It is also distinct from the Strategy-to-PM guard at STEP 4.
  DO NOT conflate these guards. Each fires on a different verdict value and protects
  PM evaluation from a different contamination source.

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

CROSS-STEP GUARD — Strategy to PM (C-36: Arch-first ordering Strategy-to-PM guard):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Record the cross-step guard lists:
    Blocked from PM Evaluation (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation (strategy-verdict = ADEQUATE and not Architect-blocked): [{list}]

  This is the C-36 guard. In this Arch-first ordering (Arch→Strat→PM), Strategy runs at
  STEP 4 before PM at STEP 5. Without this guard, a namespace with insufficient coverage
  adequacy for the tier would still receive PM structural completeness evaluation — a
  contamination path independent of the Architect-to-PM path addressed by C-26. This guard
  closes the coverage-adequacy contamination vector in the Arch-first design.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. It is independent of the C-26 guard (which
  fires on `architect-verdict = CONTRADICTS-ARCHITECTURE`). Both guards protect STEP 5
  from distinct contamination sources; both apply in this Arch-first design.
  DO NOT conflate the Strategy-to-PM guard (C-36, fires on Strategy verdict) with the
  Architect-to-PM guard (C-26, fires on Architect verdict). They are structurally parallel
  but independently triggered.

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and C-36 cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces that cleared BOTH cross-step guards:
  — architect-verdict = CONSISTENT-WITH-ARCHITECTURE (C-26 guard cleared)
  — strategy-verdict = ADEQUATE FOR TIER {tier} (C-36 guard cleared)
Namespaces on either guard's blocked list DO NOT proceed to PM evaluation. Applying
PM evaluation to a guard-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

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
        Tense/component test: the third component uses present-tense artifact-state form
          with artifact as grammatical subject. A third component in past-tense with a
          role as subject is a VERDICT-ECHO-IN-NEXT-STEPS — a distinct error from
          TRACEABILITY-BREAK but equally void. Two named error classes at this template site:
            TRACEABILITY-BREAK: entry has 2 components (third slot absent).
            VERDICT-ECHO-IN-NEXT-STEPS: entry has 3 components but third uses role-subject,
              past-tense (e.g., "Architect found no gate" rather than "Section 4.1 has no gate").
          Neither is a valid entry; both require rewrite before this section is complete.
        This classification is deterministic from entry structure — no content judgment
          required. Breaking the end-to-end chain (SQ answer → Artifact state field →
          next-steps entry) at the final link is the TRACEABILITY-BREAK error.

    CROSS-TEMPLATE ERROR SYMMETRY DECLARATION:
      VERDICT-ECHO-IN-NEXT-STEPS is the parallel error to VERDICT-ECHO.
      Both errors implement the same classification principle: a role or verdict used as
      grammatical subject produces a void content slot. The principle is applied at two
      structurally distinct template sites:
        VERDICT-ECHO — template site: `SQ answer driving verdict` field in STEP 6
          REAL-REQUIRED block.
          Classification test: grammatical subject is a role label (Architect, PM, Strategy,
          or any evaluation noun) → VERDICT-ECHO. The field must name an artifact in
          present-tense state; a role performing a past-tense assessment is void.
        VERDICT-ECHO-IN-NEXT-STEPS — template site: `{Artifact state}` slot in this
          STEP 7 entry format.
          Classification test: third component uses a role as grammatical subject in
          past tense → VERDICT-ECHO-IN-NEXT-STEPS. The slot must name an artifact in
          present-tense state; a role performing a past-tense assessment is void.
      This symmetry declaration appears here, in the entry format template definition,
      making the cross-template relationship structurally visible at this site. The
      declaration is not a prose note — it is a named structural block that names both
      template sites, both classification tests, and the shared principle. A reader at
      this STEP 7 template site can verify both error classes and their relationship
      without cross-referencing STEP 6.

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
```

---

## Design Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | output-format | role-sequence | lifecycle-emphasis | role-seq + phrasing | lifecycle + inertia |
| **Ordering** | Arch→Strat→PM | Strat→Arch→PM | Arch→Strat→PM | Strat→Arch→PM | Arch→Strat→PM |
| **C-36** | FAIL (absent) | UNREACHABLE | PASS | UNREACHABLE | **PASS** |
| **C-37** | PASS | FAIL (absent) | FAIL (absent) | PASS | **PASS** |
| **C-35** | UNREACHABLE | PASS | UNREACHABLE | PASS | UNREACHABLE |
| **C-26** | PASS | PASS | PASS | PASS | PASS |
| **C-34** | PASS | PASS | PASS | PASS | PASS |

**Single-axis discriminations:**
- V-01 isolates C-37 in Arch-first context — tests whether the symmetry declaration block alone satisfies C-37 independent of guard changes
- V-02 isolates C-35 in Strat-first context with C-26 preserved — re-confirms C-35 with full C-34 coverage (R12 V-02 failed C-34)
- V-03 isolates C-36 in Arch-first context — tests whether the named Strategy-to-PM gate in Arch-first ordering satisfies C-36 independent of C-37

**Predicted ceiling:** V-05 — Arch-first canonical design with both C-36 and C-37 present, strongest structural guarantees, full R12 V-01 criteria preserved. The C-36 guard and C-37 declaration are independent additions at STEP 4 and STEP 7 respectively; neither requires structural changes to any other step.
