# mock-review — QU5 Simplification Pass (R20 V-01)

**Date:** 2026-03-16
**Source:** mock-review-variate-R20-2026-03-16.md V-01
**Rubric target:** v21 (C-01 through C-44; essential denominator = 5)

---

## Simplification report

| Item | Removed | Words saved |
|------|---------|-------------|
| Frontmatter block | skill/date/round/rubric_version/status YAML | ~12 |
| "What R19 Left Open" section | Full section (R19 analysis, C-42/C-43 target table) | ~170 |
| Variation Axes and Hypotheses section | Full table + column headers | ~180 |
| V-01 per-variation preamble | axis / hypothesis / C-42 / C-43 metadata blocks | ~140 |
| V-02 full variation body | C-42 FAIL prompt (Strategy-first) | ~1,800 |
| V-03 full variation body | C-42 PASS + inertia-heavy prompt (RESISTANCE CHECK) | ~2,000 |
| V-04 full variation body | C-42 PASS + conversational register prompt | ~2,100 |
| V-05 full variation body | C-42 PASS + belt-and-suspenders prompt | ~2,200 |
| All `<!-- C-42: ... -->` HTML comments (9 occurrences) | Aspirational C-42 labeling annotations | ~280 |
| Criterion-ID annotations in step headings (12 occurrences) | `(C-07, C-13, C-36)` etc. — documentation only | ~65 |
| `[C-NN]` inline labels in template slot headers | `(C-23, C-30)`, `(C-20, C-25)` etc. in STEP 6 body | ~30 |
| `[C-NN]` inline labels in TRIAD / guard headers | C-38/C-40/C-41/C-43 in CROSS-TEMPLATE block | ~25 |
| CROSS-TEMPLATE block HTML comment | `<!-- C-38: ... C-41 + C-43: ... -->` | ~30 |
| "This guard fires on ... Arch-first design: C-36 ✓, C-35 N/A." | Explanatory sentence — condition already stated above | ~30 |
| "Header: Topic \| Tier \| Date" redundant label in STEP 7 | Covered by the file template line | ~6 |
| CANARY verbose error expansion | "— writing the canary when the condition is not met" | ~10 |

**What was NOT removed:** DEFAULT DECISION POSITION (inertia framing), FORBIDDEN OUTPUTS TRIAD
with 3 exact labels, AUTO-RULE CONTAMINATION GUARD, all three cross-step guards with Record
blocks, CROSS-TEMPLATE RELATIONSHIP BLOCK (drives C-03 reason-code placement), both MOCK-ACCEPTED
slots (SLOT-VIOLATION / CONTRAST-INCOMPLETE guards), REAL-REQUIRED template fields, Row # column
in eval tables (low-cost, high-traceability), all DO NOT proceed gates, CANARY assertion + CANARY
SUPPRESSED path, full confirmation block.

**Rationale:** Items removed are (a) variate testing scaffolding not part of the skill definition,
(b) C-42 HTML comments whose only purpose is to document aspirational criterion coverage,
(c) criterion-ID parenthetical annotations that are documentary cross-references rather than
behavioral instructions, and (d) single redundant explanatory sentences whose content is
restated by the instruction they follow.

---

## Simplified prompt body

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
