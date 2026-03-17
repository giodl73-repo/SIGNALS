---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 3
rubric_version: v3
status: VARIATE
---

# mock-review Variate — Round 3

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v3 (C-01 through C-16; aspirational denominator = 8)
**Round:** R3 — targeting v3 new criteria: C-14, C-15, C-16

---

## What R2 Left Open

R2 variations closed C-11 (forbidden-output for all three rules), C-12 (count-and-confirm
verification output), and C-13 (verifiable role-step separation with sub-questions and STOP
gates). Three new aspirational criteria were introduced in v3 based on scorecard evidence:

| Criterion | Best R2 coverage | Gap |
|-----------|-----------------|-----|
| C-14 Sub-question answer citation | V-04 STEP 6: "Name the specific evaluation that failed and the sub-question answer that drove it" | Instructional text only — no output template slot forces the model to produce the sub-question answer in the verdict. A model can write "REAL-REQUIRED — Architect: CONTRADICTS KNOWN FACTS" and satisfy the instruction while omitting the sub-question answer. |
| C-15 Entity-naming sub-question grammar | V-03/V-04: "Name at least one section", "Name the specific gate", "Name one specific element" | Sub-questions still have yes/no opener clauses ("Are all required sections present?") before the naming follow-up. C-15 requires the sub-question grammar itself to force naming — no yes/no gate, only "Name X" or "What specific X" forms throughout. |
| C-16 Canary confirmation (prohibited under failure) | V-02: "MUST NOT be written if any field missed" | Prohibition is present but canary framing is absent. C-16 requires the confirmation to be a named canary: its presence asserts the condition; writing it under failure is a named protocol error. R2 V-02 has the prohibition without the named-error semantics. |

R3 targets each gap with a dedicated single-axis variation, then combines them.

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | phrasing-register | C-15 gap: yes/no opener clauses precede entity-naming follow-ups in R2 sub-questions | C-15, C-07 | All sub-questions written in "Name X" / "What specific X" form; yes/no openers removed; C-15 passes cleanly |
| V-02 | lifecycle-emphasis | C-16 gap: prohibition present but canary-output semantics absent in R2 V-02 | C-16, C-12 | Zero-remaining confirmation named as a canary output; its false-positive condition named as a protocol error; C-16 passes as canary not just checkbox |
| V-03 | output-format | C-14 gap: instructional "name the sub-question answer" produces no structural guarantee of citation in output | C-14, C-06 | Pre-printed REAL-REQUIRED verdict template with dedicated [SUB-QUESTION ANSWER] slot; model cannot produce the verdict without filling the slot |
| V-04 | phrasing-register + output-format | Combine V-01 entity-naming grammar with V-03 citation template | C-14, C-15, C-07 | Entity-naming sub-questions produce artifact-specific answers; citation template routes those answers into the verdict; traceable chain from sub-question to decision |
| V-05 | phrasing-register + output-format + lifecycle-emphasis | V-01 entity-naming + V-03 citation template + V-02 canary framing + R2 V-01 forbidden-output (C-11) + R2 V-03 step separation (C-13) | C-14, C-15, C-16, C-11, C-13 | Ceiling combination: all five criteria addressed; each through a structural guarantee rather than an instruction |

---

## V-01 — Entity-Naming Sub-Question Grammar

**axis:** phrasing-register
**hypothesis:** R2 V-03 and V-04 made progress on C-15 by adding naming follow-ups to
sub-questions ("Name at least one section that is present", "Name the specific gate").
However, each sub-question still opens with a yes/no-answerable clause: "Are all required
sections present?" — which a model can satisfy with "Yes" before adding the naming follow-up,
or omit the follow-up entirely. C-15 requires the sub-question grammar itself to be in
entity-naming form: every sub-question uses "Name X" or "What specific X" so that the only
possible answer is a named artifact. Removing yes/no openers eliminates the shortcut. For PM:
"Name the required sections present" forces an answer like "Sections: Overview, Gate Definition,
Status Table" rather than "Yes, sections are present." For Architect: "Name the system
component confirmed as plausible" forces "Component: EventBus" rather than "Yes, plausible."
For Strategy: "Name the specific Tier {tier} decision this namespace supports" forces a
named decision rather than a general coverage adequacy judgment. Expected improvement:
C-15 PASS (all sub-questions in entity-naming form), C-07 improvement (PM sub-questions
reference named sections, Architect names specific components). Failure condition: if the
model still answers with yes/no despite the entity-naming form, the phrasing alone is
insufficient and a mandatory one-artifact minimum requirement is needed.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier} — from --tier flag, TOPICS.md, or default 1

**Setup**

Read {mock-artifact-path}.
For each namespace section, extract: namespace name, Category (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED), current Status.
Read TOPICS.md: tier for {topic}, compliance tags.
State at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"

**Phase 1 — Automatic Flagging**

Apply all three rules before any role evaluation. Rules are mandatory and not role-overridable.

RULE A — EVIDENCE-HEAVY (all tiers):
  Condition: Category == EVIDENCE-HEAVY
  Action: REAL-REQUIRED, trigger = EVIDENCE-HEAVY

RULE B — TIER-CRITICAL (Tier 2 and Tier 3 only):
  Condition: tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  Action: REAL-REQUIRED, trigger = TIER-CRITICAL

RULE C — COMPLIANCE (when compliance context is active):
  Condition: compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  Action: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists before Phase 2:

  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting Phase 2 evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

Every namespace in exactly one list. Do not begin Phase 2 until both lists are complete.

**Phase 2 — Role Evaluation (non-auto namespaces)**

For each namespace in the Remaining list, complete three separately executable evaluations.
Each evaluation produces its own verdict. Do not combine evaluations into a single block.
Complete all PM verdicts before beginning Architect. Complete all Architect verdicts before
beginning Strategy.

--- PM Evaluation — Structural Completeness ---

For each namespace, answer these sub-questions then write the PM verdict:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure that is
        present and correctly formed (or: "None found — [name what is absent]").
  SQ-3: Name one structural gap that would prevent a PM from accepting this mock as
        Tier {tier} coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM verdicts for all remaining namespaces before beginning Architect evaluation.

--- Architect Evaluation — Technical Plausibility ---

For each namespace, answer these sub-questions then write the Architect verdict:

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility with {topic} architecture (or: "Contradiction found — [name the element]").
  SQ-2: Name the data flow, state transition, or API shape that is consistent with {topic}
        (or: "Inconsistency found — [name it]").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect verdicts for all remaining namespaces before beginning Strategy evaluation.

--- Strategy Evaluation — Coverage Adequacy ---

For each namespace, answer these sub-questions then write the Strategy verdict:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief is correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment if this mock is
        accepted (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy verdicts for all remaining namespaces before Phase 3.

**Phase 3 — Decisions**

For each non-auto namespace, combine the three verdicts:

  All verdicts positive:
    MOCK-ACCEPTED — include at least one exact reason code:
      STRUCTURAL-COVERAGE-SUFFICIENT  (structural completeness drove the verdict)
      DOMAIN-KNOWLEDGE-CONSISTENT     (content plausibility drove the verdict)
    No paraphrase. No invented codes. Use both when both apply.
    Include one sentence stating why the reason code applies to this specific namespace.

  Any verdict negative:
    REAL-REQUIRED — name the evaluation that failed and the verdict.

**Phase 4 — Write Review Artifact**

Write simulations/mock/{topic}-review-{date}.md:

  Section 1 — Header: Topic | Tier | Date
  Section 2 — Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    All namespaces from Phases 1 and 3.
  Section 3 — Next Steps (numbered, priority order):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill} {topic} — {one-line reason}

**Phase 5 — Write Status Back (mandatory)**

For every namespace in {mock-artifact-path}, use Edit to replace the Status line in-place:
  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

Edit the Status line only. No other content in the source artifact changes.
This is the defining action of /mock:review.

After all edits, confirm:
  "Annotations updated in: {mock-artifact-path}"
  "Review written: simulations/mock/{topic}-review-{date}.md"
  "Status fields updated: {N} of {N}"
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If any Status field was not updated, DO NOT write the count-zero confirmation.
List each namespace whose Status was not updated, then attempt the edits again.

---

## V-02 — Canary Confirmation Framing

**axis:** lifecycle-emphasis
**hypothesis:** R2 V-02 introduced the prohibition: "This confirmation line is required. If
any Status field was not updated, the confirmation MUST NOT be written." This is a behavioral
rule — a constraint on what the model may produce. C-16 requires more: the zero-remaining
confirmation is a CANARY OUTPUT. A canary output is not merely required on success and
prohibited on failure; it is a output whose presence actively asserts that the success
condition has been met. This means: (1) writing the canary when the condition is not met
is a protocol error with a name, not just a rule violation, and (2) a reviewer inspecting
the output can detect the error by checking whether the asserted condition holds. R2 V-02
has the prohibition but not the named-error semantics. Adding a named error — CANARY-FALSE-
POSITIVE — transforms the confirmation from a checkbox into a verifiable assertion. Expected
improvement: C-16 PASS (canary framing with named error), C-12 PASS (zero-remaining
confirmation remains required on success). Failure condition: if the model produces the
canary line regardless of completion state, the named error adds no enforcement — the
behavioral pattern has not changed, only the label.

---

You are running /mock:review.

Input:
  Topic:         {topic}
  Mock artifact: {mock-artifact-path}
  Tier:          {1|2|3} — from --tier flag, TOPICS.md, or default 1

### PHASE 1 — READ AND CLASSIFY

Read {mock-artifact-path}. Extract: namespace name, Category, current Status per namespace.
Read TOPICS.md: tier for {topic}, compliance tags.
Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
Output namespace inventory: | Namespace | Category | Current Status |

STOP. Do not enter Phase 2 until the namespace inventory is complete.

---

### PHASE 2 — AUTO-FLAGGING

Apply all three rules before any role evaluation. Rules are mandatory and not role-overridable.

  EVIDENCE-HEAVY (all tiers): Category == EVIDENCE-HEAVY → REAL-REQUIRED, trigger: EVIDENCE-HEAVY
  TIER-CRITICAL (Tier 2+ only): tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*,
    scout-competitors} → REAL-REQUIRED, trigger: TIER-CRITICAL
  COMPLIANCE (when compliance context active): compliance tags in TOPICS.md OR --compliance flag
    AND namespace in {scout-compliance, trace-permissions} → REAL-REQUIRED, trigger: COMPLIANCE

Output:
  Auto-flagged (REAL-REQUIRED): {namespace}: trigger = {rule label}
  Remaining (awaiting Phase 3): {namespace}: Category = {HIGH-STRUCTURE | MIXED}

STOP. Every namespace in exactly one list before entering Phase 3.

---

### PHASE 3 — THREE-ROLE EVALUATION

For each namespace in the Remaining list:

  PM: Are required sections present? Are enforcement gates and tables well-formed?
    Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

  Architect: Does content contradict known architectural facts about {topic}?
    Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

  Strategy: Is coverage adequate for Tier {tier} decisions?
    Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

  Decision:
    All verdicts positive → MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT |
                                          DOMAIN-KNOWLEDGE-CONSISTENT]
    Any verdict negative → REAL-REQUIRED [failed evaluation verdict]

  Reason codes are exact. No paraphrase.

STOP. All remaining namespaces must have decisions before entering Phase 4.

---

### PHASE 4 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:
  Section 1 — Header: Topic | Tier | Date
  Section 2 — Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    All namespaces from Phases 2 and 3.
  Section 3 — Next Steps (numbered, priority order):
    Priority 1: Critical REAL-REQUIRED: trace-* first, scout-feasibility, listen-*
    Priority 2: Non-critical REAL-REQUIRED
    Priority 3: Evidence-heavy REAL-REQUIRED
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill} {topic} — {one-line reason}

STOP. Review artifact must be written before entering Phase 5.

---

### PHASE 5 — WRITE STATUS BACK (mandatory)

This is the defining action of /mock:review. It cannot be skipped.

For every namespace in {mock-artifact-path}, use Edit to update the Status line in-place:
  Replace: Status: MOCK (awaiting review)
  With one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger or evaluation reason}]

Rules:
  - Edit the Status line only. No other content in the source artifact changes.
  - This is the only permitted in-place edit in Signal.
  - Each written Status must match the Coverage Review table from Phase 4.

**Canary Confirmation — output protocol:**

The following line is a CANARY OUTPUT:

  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

A canary output is an assertion, not a checklist item. Writing this line claims that the
stated condition is true. The claim is verifiable by inspection — a reviewer can read
{mock-artifact-path} and confirm whether the condition holds.

Protocol rules:
  1. Write the canary ONLY when every Status field in {mock-artifact-path} has been updated
     and confirmed as no longer MOCK (awaiting review).
  2. Writing the canary when any Status field remains as MOCK (awaiting review) is a
     protocol error named CANARY-FALSE-POSITIVE. This error is detectable: the canary
     line is present but the asserted condition is false.
  3. If any Status field was not updated: suppress the canary and output instead:
       "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
     Then attempt the remaining edits. When all edits are confirmed, write the canary.

Full confirmation block (written only when canary condition is verified true):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Sub-Question Answer Citation Template

**axis:** output-format
**hypothesis:** R2 V-04 STEP 6 states: "Name the specific evaluation that failed and the
sub-question answer that drove it." This is an instruction. An instruction can be satisfied
by mentioning the failing evaluation name without producing a traceable sub-question answer
— e.g., "REAL-REQUIRED — Architect: CONTRADICTS KNOWN FACTS (sub-question answer: element
is inconsistent)". The phrase "element is inconsistent" names no specific artifact; it is a
restatement of the verdict. C-14 requires the output to name the specific sub-question answer
that drove the verdict — not a paraphrase of the verdict, but the actual answer to a specific
sub-question. A pre-printed verdict template with a dedicated [SUB-QUESTION ANSWER] slot makes
this structural: the model cannot produce a REAL-REQUIRED decision template without filling a
slot that requires the sub-question answer by position. The slot is distinct from the verdict
slot — filling "CONTRADICTS KNOWN FACTS" in one slot and "EventBus dependency absent" in the
other is structurally forced. Expected improvement: C-14 PASS (citation template makes
sub-question answer a required output field), C-06 improvement (evaluation-driven REAL-REQUIRED
decisions now contain the diagnostic answer, not just the evaluation name).
Failure condition: if the model fills the [SUB-QUESTION ANSWER] slot with a restatement of
the verdict ("the facts were contradicted") rather than a genuine sub-question answer, the
template is syntactically satisfied but semantically empty — in which case C-14 requires a
"must name a specific artifact" constraint in the slot label.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier} — from --tier flag, TOPICS.md, or default 1

**Setup**

Read {mock-artifact-path}. For each namespace section, extract: namespace name, Category, current Status.
Read TOPICS.md: tier for {topic}, compliance tags.
State: "Tier: {N} (source: TOPICS.md | --tier | default)"

**Phase 1 — Automatic Flagging**

Apply all three rules before any evaluation. Rules are mandatory and not overridable by role.

  EVIDENCE-HEAVY (all tiers): Category == EVIDENCE-HEAVY → REAL-REQUIRED, trigger: EVIDENCE-HEAVY
  TIER-CRITICAL (Tier 2+): tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*,
    scout-competitors} → REAL-REQUIRED, trigger: TIER-CRITICAL
  COMPLIANCE: compliance context active AND namespace in {scout-compliance, trace-permissions}
    → REAL-REQUIRED, trigger: COMPLIANCE

Output before Phase 2:
  Auto-flagged (REAL-REQUIRED): {namespace}: trigger = {rule label}
  Remaining (awaiting Phase 2): {namespace}: Category = {HIGH-STRUCTURE | MIXED}

Every namespace in exactly one list. Do not enter Phase 2 until lists are complete.

**Phase 2 — Role Evaluation (non-auto namespaces)**

For each namespace in the Remaining list:

  PM:
    Are required sections present? Are enforcement gates, decision tables, or output structures
    present and well-formed? Would a PM accept this as Tier {tier} structural coverage?
    Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

  Architect:
    Does mock content contradict known architectural facts about {topic}?
    Are data flows, state transitions, and API shapes consistent with {topic}?
    Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

  Strategy:
    Would a team making Tier {tier} decisions be adequately served by this mock?
    Is there any decision the team might make incorrectly if this runs as MOCK-ACCEPTED?
    Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

**Phase 3 — Decisions with Required Citation**

For each non-auto namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (use exact codes only; include both when both apply; no paraphrase)
  Rationale: [One sentence explaining why the reason code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[Exact answer produced by the failing sub-question
    — name the specific section, element, or gap, not a restatement of the verdict]"

  This template is required for every evaluation-driven REAL-REQUIRED decision.
  A REAL-REQUIRED decision that omits the sub-question answer field is incomplete.

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]
  No sub-question citation required for auto-flagged decisions.

**Phase 4 — Write Review Artifact**

Write simulations/mock/{topic}-review-{date}.md:

  Section 1 — Header: Topic | Tier | Date
  Section 2 — Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    All namespaces from Phases 1 and 3.
  Section 3 — Next Steps (numbered, priority order):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill} {topic} — {one-line reason citing the sub-question answer for evaluation-driven decisions}

**Phase 5 — Write Status Back (mandatory)**

For every namespace in {mock-artifact-path}, use Edit to replace the Status line in-place:
  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

Edit the Status line only. No other content in the source artifact changes.
This is the defining action of /mock:review.

After all edits complete:
  Confirm: "Annotations updated in: {mock-artifact-path}"
  Confirm: "Review written: simulations/mock/{topic}-review-{date}.md"
  Confirm: "Status fields updated: {N} of {N}"
  Confirm: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If any Status field was not updated, DO NOT write the count-zero confirmation.
List each namespace not updated and attempt the remaining edits before re-confirming.

---

## V-04 (Combined) — Entity-Naming Grammar + Sub-Question Answer Citation

**axes:** phrasing-register + output-format
**hypothesis:** V-01 entity-naming sub-questions ("Name X", "What specific X") force the model
to produce an artifact-specific answer as its first response to each sub-question — a section
name, a component name, a decision name. V-03 verdict citation template routes those artifact-
specific answers into a dedicated slot in the REAL-REQUIRED verdict. The combination creates
a traceable chain: sub-question → named artifact answer → verdict citation. V-01 alone satisfies
C-15 but does not guarantee the named artifact flows into the verdict (the model names it
during evaluation but may summarize it away in the decision). V-03 alone satisfies C-14 but
the [SUB-QUESTION ANSWER] slot may still be filled with a verdict restatement if the sub-
questions permit yes/no openers. Together: the entity-naming grammar produces a specific artifact
answer, and the citation template enforces that this specific answer appears in the verdict slot.
Expected: C-14 PASS (citation slot enforced by template), C-15 PASS (all sub-questions in
entity-naming form), C-07 improvement (PM references named sections, Architect names components,
Strategy names specific decisions). Failure condition: the model fills the citation slot with
a generic artifact name unconnected to the evaluation outcome — e.g., "EventBus" for a PM
structural gap — meaning the slot is filled but not causally connected to the verdict.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

---

STEP 3 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict:

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier {tier}
        coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to Step 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict:

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to Step 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict:

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

---

STEP 6 — DECISIONS WITH CITATION

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer that produced the
    negative verdict — name the specific section, element, gap, or decision, not a restatement
    of the verdict]"

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; cite the sub-question answer for evaluation-driven}

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

After all edits:
  MUST confirm: "Annotations updated in: {mock-artifact-path}"
  MUST confirm: "Review written: simulations/mock/{topic}-review-{date}.md"
  MUST confirm: "Status fields updated: {N} of {N}"
  MUST confirm: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If any Status field was not updated: DO NOT write the count-zero confirmation.
List each namespace whose Status was not updated, then attempt remaining edits.
This is the defining action of /mock:review. It is not optional.

---

## V-05 (Combined) — Ceiling: C-14 + C-15 + C-16 + C-11 + C-13

**axes:** phrasing-register + output-format + lifecycle-emphasis
**hypothesis:** R2's best performers closed C-11 (V-01: forbidden-output for all three rules),
C-12 (V-02: count-and-confirm), and C-13 (V-03/V-04: step separation with sub-questions).
R3's V-01, V-02, V-03 address C-15, C-16, C-14 independently. The ceiling combination adds
all three R3 axes to the R2 V-04 base (which had forbidden-output and step separation):
  - Entity-naming sub-question grammar from V-01 (C-15)
  - REAL-REQUIRED citation template from V-03 (C-14)
  - Canary confirmation with named error from V-02 (C-16)
  - Forbidden-output DO NOT statements from R2 V-01/V-04 (C-11)
  - Separately completable role steps with STOP gates from R2 V-03/V-04 (C-13)
This creates the highest-coverage variation against the v3 rubric. The structural risk is
length-driven compliance drift — a prompt covering five criteria is longer, and models may
deprioritize later phases (write-back, priority ordering) when the evaluation phase absorbs
attention. The pre-printed template approach from R2 V-05 mitigates this: pre-printed role
sections exist regardless of model attention, and the canary framing enforces write-back
completion rather than just requesting it. Expected: C-11, C-12, C-13, C-14, C-15, C-16
all PASS; C-01 through C-08 maintained. Failure condition: the sub-question answer citation
slot is filled but the canary line is produced before the write-back edits are verified,
meaning the canary framing applies correctly in the rule text but fails behaviorally.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  mock content depth, or PM/Architect/Strategy evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any compliance-tagged namespace MOCK-ACCEPTED when compliance context
  is active. Compliance signals require real evidence; mock artifacts do not produce them.

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

---

STEP 3 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier {tier}
        coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to Step 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to Step 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

---

STEP 6 — DECISIONS WITH CITATION

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; for evaluation-driven: cite the sub-question answer}

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

After completing all edits, verify before confirming.

**Canary Confirmation — output protocol:**

The following line is a CANARY OUTPUT:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

This line is an assertion that the stated condition is true. Its presence claims that every
Status field in {mock-artifact-path} has been updated. Writing this line when any Status
field remains as MOCK (awaiting review) is a protocol error named CANARY-FALSE-POSITIVE.
This error is detectable by inspection of {mock-artifact-path}.

Protocol:
  - Write the canary ONLY after confirming that zero Status fields remain as MOCK.
  - If any Status field was not updated: suppress the canary. Output instead:
      "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
    Attempt the remaining edits. Re-verify. Then write the canary when condition is met.

Full confirmation block (only when canary condition is verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

This is the defining action of /mock:review. It is not optional.

---

## Variation Map Summary

| V | Axes | What Changed | Target Criteria | Hypothesis |
|---|------|--------------|-----------------|------------|
| V-01 | phrasing-register | All PM/Architect/Strategy sub-questions rewritten in "Name X" / "What specific X" form; yes/no opener clauses removed | C-15, C-07 | Entity-naming grammar forces artifact-specific answers; yes/no shortcut eliminated; C-15 passes as sub-question grammar not just content |
| V-02 | lifecycle-emphasis | Zero-remaining confirmation named as a canary output; false-positive condition named CANARY-FALSE-POSITIVE; suppression protocol on failure | C-16, C-12 | Canary framing makes the confirmation an assertion, not a checkbox; named error makes it falsifiable; C-16 passes as canary not just prohibition |
| V-03 | output-format | Pre-printed REAL-REQUIRED verdict template with dedicated "Sub-question answer that drove this verdict" slot | C-14, C-06 | Structural slot forces sub-question answer as a required output field; model cannot produce the verdict without filling the citation slot |
| V-04 | phrasing-register + output-format | V-01 entity-naming sub-questions combined with V-03 citation template | C-14, C-15, C-07 | Entity-naming grammar produces the artifact answer; citation template routes it into the verdict; traceable chain from sub-question to decision |
| V-05 | phrasing-register + output-format + lifecycle-emphasis | All three R3 axes (C-15, C-14, C-16) combined with R2 V-04 forbidden-output (C-11) and step separation (C-13) | C-11, C-13, C-14, C-15, C-16 | Ceiling combination; each criterion addressed through a structural guarantee; all five enforced simultaneously |

**Top combination candidate for Round 4:**
If V-05 achieves the highest composite, the next test is whether V-05's length creates
C-05 ordering regressions (models deprioritizing next-steps ordering when evaluation phases
are exhaustive). A focused R4 variation isolating the Next Steps section — pre-printing the
Priority 1/2/3 headers as a skeleton similar to R2 V-05's PHASE 7 — is worth testing as a
single axis against the ceiling combination.
