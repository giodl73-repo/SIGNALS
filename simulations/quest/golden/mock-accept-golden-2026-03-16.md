---
skill: quest-golden
skill_target: mock-review
date: 2026-03-15
rounds: 20
rubric_final: mock-review-rubric-v21-2026-03-16.md
score: 99
status: GOLDEN
---

# mock-review — Golden Prompt (R20 V-01, QU5 Simplified)

**Date:** 2026-03-16
**Rounds:** 20
**Winning variation:** R20 V-01 (Arch-first, C-42 PARTIAL, C-43 PASS)
**Simplification:** PASS — 87% reduction (11,649 → 1,459 words)
**Score:** 99.05 / 100 → **99**

---

## Golden Prompt

```
You are running /mock:review.

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

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 until Architect verdicts and guard assignments are complete
for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete
for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

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
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — MOCK-ACCEPTED exits before next-steps)  |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint:
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.
  "Section 4.1 contains no tier-boundary gate" = valid. "Architect found no gate" = VERDICT-ECHO.

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Structural position (SLOT 1 — Strategy SQ-1 anchor):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

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

Write simulations/mock/{topic}-review-{date}.md.
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
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## What Made It Golden

**5 patterns that distinguish V-01 from the baseline:**

### 1. DEFAULT DECISION POSITION as a named inversion block (C-22)
Earlier versions treated MOCK-ACCEPTED and REAL-REQUIRED as symmetric outcomes evaluated in parallel. V-01 establishes a named block at the top of the skill that declares REAL-REQUIRED as the starting position and MOCK-ACCEPTED as an escape requiring a positive argument against inertia. The block names the failure mode explicitly: "confirmation that nothing is wrong does not earn MOCK-ACCEPTED." This forces genuine contrastive reasoning at every evaluation step rather than symmetric comparison.

### 2. FORBIDDEN OUTPUTS TRIAD co-located at the PHASE GATE (C-27 + C-29)
Earlier versions distributed DO NOT statements across role steps, tying their verifiability to step position. V-01 places a single TRIAD block with three individually labeled forbidden-output statements immediately at the phase gate separating automatic rules from role evaluation. The three labels — `[EVIDENCE-HEAVY]`, `[TIER-CRITICAL]`, `[COMPLIANCE]` — are enumerable in one scan. This design decouples the TRIAD from role ordering: any role sequence satisfies C-27 because the TRIAD sits at the boundary, not inside a role step.

### 3. Dual-slot MOCK-ACCEPTED template closing the confirmatory escape (C-25 + C-30)
Earlier versions used a single `Rationale:` slot for MOCK-ACCEPTED justification, which allowed a confirmatory sentence ("structural coverage is sufficient here") to satisfy the slot. V-01 mechanically separates the rationale into two distinct, labeled slots: SLOT 1 (Structural position — SQ-1 anchor naming the specific tier decision) and SLOT 2 (Contrast — explicitly requires naming a contrasting namespace type and the structural factor that distinguishes it). A single-slot answer physically cannot satisfy both slots, closing the confirmatory escape structurally rather than through advisory instruction.

### 4. Three chained cross-step guards with named contamination errors (C-26 + C-17 + C-18)
Earlier versions separated phases but did not name the contamination errors for inter-role guard violations. V-01 adds named errors at every guard boundary: `ARCH-GUARD-BYPASS` (Architect blocks Strategy), `STRATEGY-TO-PM-GUARD-BYPASS` (Strategy blocks PM), and `GUARD-BYPASS CONTAMINATION` (entry condition for STEP 4 and STEP 5). Each guard also includes a Record block listing both the blocked namespaces and the namespaces proceeding forward — making the guard state a named, verifiable intermediate output rather than an implicit condition.

### 5. CANARY assertion as a falsifiable mechanical claim (C-16 + C-12)
Earlier versions used a confirmation block that was structurally optional — it appeared as a summary statement rather than a conditional assertion. V-01 makes the canary output explicitly conditional: the CANARY ASSERTION is `PROHIBITED if any Status field remains as MOCK`, and writing it when the condition is not met is a named error: `CANARY-FALSE-POSITIVE`. The `CANARY SUPPRESSED` path provides the failure-case output. This converts the confirmation from a reporting element into a falsifiable claim whose presence is evidence of the condition being met.

---

## Final Rubric Criteria Summary (v21)

**Formula:** `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/38 × 10)`
**PARTIAL** = 0.5 credit.

### Essential — 60 pts

| ID | Name |
|----|------|
| C-01 | Decision completeness — every namespace in exactly one list |
| C-02 | Automatic rule correctness — three rules fire before role evaluation; non-overridable |
| C-03 | MOCK-ACCEPTED reason code present — exact enumeration only, no paraphrase |
| C-04 | Status fields written back — in-place Edit tool; mandatory non-skippable phase |
| C-05 | Next-steps list in priority order — ordering rule stated explicitly |

### Recommended — 30 pts

| ID | Name |
|----|------|
| C-06 | Rule trigger named per REAL-REQUIRED — `trigger = {rule}` field at fixed position |
| C-07 | PM / Architect / Strategy evaluation shown — all three roles, own heading + verdict |
| C-08 | Tier flag respected — stated at top with source; TIER-CRITICAL gates on Tier >= 2 |

### Aspirational — 10 pts (denominator 38)

| ID | Name |
|----|------|
| C-09 | Coverage gap synthesis — cross-namespace risk statement + urgency grouping commentary |
| C-10 | Namespace-specific MOCK-ACCEPTED rationale — explanatory sentence per namespace |
| C-11 | Forbidden-output enumeration for auto-rules — named DO NOT per rule, not generic |
| C-12 | Zero-remaining confirmation gate — explicit verification step, required output |
| C-13 | Verifiable role-step separation — each role separately completable with own verdict |
| C-14 | Sub-question answer citation in verdict traceability — SQ answer names the specific driver |
| C-15 | Entity-naming sub-question grammar — "Name X" / "What specific X" forms required |
| C-16 | Canary confirmation — PROHIBITED under failure; named error CANARY-FALSE-POSITIVE |
| C-17 | Auto-flagged contamination guard — names the contamination error, not just the trigger |
| C-18 | Inter-step gate with next-step reference — forward reference to named next step |
| C-19 | Structured trigger notation — named parseable field at fixed position |
| C-20 | Contrastive MOCK-ACCEPTED rationale — explains why this namespace does not cross threshold |
| C-21 | SQ answer structural signal — artifact-as-subject distinguishes from verdict-echo |
| C-22 | Decision inversion framing — REAL-REQUIRED as default; MOCK-ACCEPTED as earned escape |
| C-23 | Strategy SQ-1 anchor in Structural position — names specific tier decision as slot source |
| C-24 | Artifact state field propagation into next-steps — `/{skill} {topic} — {Artifact state}` |
| C-25 | Dedicated contrast sub-slot — SLOT 2 structurally separate from SLOT 1 |
| C-26 | Role-sequence gate as contamination control — Arch before PM; names verdict value + blocked step |
| C-27 | Triad DO NOT coverage — complete enumerable set: one named DO NOT per rule label |
| C-28 | Step-name anchor in forward reference — number + descriptive label in gate |
| C-29 | Phase-gate co-location of forbidden-output block — TRIAD at boundary, independent of role order |
| C-30 | SQ-1 sourcing label in Structural position slot — citation field, not example |
| C-31–C-34 | *(established in prior rounds — all variants PASS; baseline)* |
| C-35 | Strategy-first tier anchoring before Arch — tier anchor exists before structural check |
| C-36 | Arch-first before Strategy for structural contradiction gating — Arch blocks Strategy on CONTRADICTS-ARCHITECTURE *(Note: C-35 and C-36 are mutually exclusive — a skill satisfies exactly one)* |
| C-37–C-41 | *(established in prior rounds — all variants PASS; baseline)* |
| C-42 | Universal criterion-ID labeling — PASS: all structural elements labeled; PARTIAL: TRIAD header alone unlabeled; FAIL: labels on template slots only |
| C-43 | Dedicated Row # column — leftmost column in all three eval-step tables; orthogonal to C-42 |
| C-44 | Mechanical inversion checklist — RESISTANCE CHECK block expands DEFAULT DECISION POSITION to enumerable, independently-testable items |
