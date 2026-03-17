---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 10
rubric_version: v10
status: VARIATE
---

# mock-accept Variate — Round 10

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v10 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-36 aspirational;
             C-34/C-35/C-36 new this round; denominator 28)
**Baseline:** R9 V-05 (sole golden, 28/28 against v10: Phase-first COST REGISTER + per-phase
             GATE E-COST assertions + DECISION SCOREBOARD live tracker)
**Round:** R10 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R9 V-05 is the sole golden at 28/28 against v10. The three R9 criteria (C-34/C-35/C-36)
tightened verifiability along the Cost Register and Scoreboard dimensions. R10 probes three
structural questions that v10's golden leaves open:

1. GATE F currently verifies only section *presence* (four sections confirmed by name).
   Does adding per-section *content* assertions — column counts, sentence counts, list
   structure — make GATE F a completeness gate rather than a presence gate? R9 V-05 checks
   the Coverage table's 4-column requirement via a CONSTRAINT inside STEP 9, but GATE F does
   not cross-verify that the written sections meet their structural requirements.

2. GATE B declares a non-flagged *count* ("Non-flagged proceeding to evaluation: ___") but
   does not name *which* namespaces form that set. STEP 3 infers the evaluation universe from
   STEP 2 context. Does an explicit named-namespace list at GATE B make the evaluation universe
   independently verifiable — decoupling STEP 3's scope declaration from STEP 2 re-reading?

3. The Architect-to-Strategy role transition is marked by GATE C's "Do not proceed to STEP 4"
   language but there is no written handoff event that enumerates the Strategy phase universe
   before STEP 4 begins. Does a named ROLE HANDOFF block between GATE C and STEP 4 — listing
   the namespaces that cleared Architect evaluation — make the role boundary a verifiable event
   rather than an inferred state transition?

| Plan | Axis | Target | What changes from R9 V-05 | Predicted |
|------|------|--------|---------------------------|-----------|
| V-01 | lifecycle-emphasis (GATE F content verification) | STEP 10 section assertions | GATE F adds per-section content checks: column count, sentence count, list structure | 28/28 |
| V-02 | output-format (GATE B evaluation-universe enumeration) | GATE B namespace list | GATE B adds explicit named-namespace list for the non-flagged evaluation set | 28/28 |
| V-03 | role-sequence (ROLE HANDOFF declaration) | STEP 4 universe declaration | Named ROLE HANDOFF block between GATE C and STEP 4 enumerates Strategy evaluation universe | 28/28 |
| V-04 | combined: GATE F content + GATE B enumeration | V-01 + V-02 | GATE F content assertions + GATE B namespace list | 28/28 |
| V-05 | combined: GATE F content + GATE B enumeration + ROLE HANDOFF | V-01 + V-02 + V-03 | All three single-axis improvements combined | 28/28 |

---

## V-01 — Lifecycle Emphasis: GATE F Section-Content Verification

**axis:** lifecycle-emphasis (GATE F content verification)
**hypothesis:** R9 V-05's GATE F verifies four section names but not their content structure.
STEP 9 CONSTRAINTs require the Coverage table to have 4 columns, Structural records to have
one sentence per namespace, Risk to carry an Urgency column, and Next Steps to be an ordered
list with three fields per entry — but these requirements are stated at write time, not
cross-verified at gate time. V-01 adds per-section content assertions inside GATE F: Coverage
table column count confirmed, Structural records sentence count confirmed (expected: 9),
Risk table column structure confirmed, Next Steps ordered-list structure confirmed. GATE F
becomes a content-completeness gate rather than a presence-only gate. All other steps
identical to R9 V-05. Predicted score against v10: 28/28.

---

You are running /mock:accept.

DECISION SCOREBOARD
  REAL-REQUIRED: 9   (all namespaces begin here — this is inertia)
  MOCK-ACCEPTED:  0   (nothing earned yet)

MOCK-ACCEPTED is earned against named evidence. The absence of a disqualification is not
evidence. Confirmation that nothing is wrong does not move a namespace off REAL-REQUIRED.
Each earned MOCK-ACCEPTED requires a positive structural or domain argument naming what makes
real data unnecessary for that namespace at this tier.

This scoreboard governs STEP 3 (Architect phase) and STEP 4 (Strategy phase).
GATE C records the Architect phase movement. GATE D records the Strategy phase movement.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

Exempt from this rule: tier sourcing output (Tier: N (source: …)); auto-flag Rule A/B/C
definition headers; verdict tokens used as classifiers (MOCK-ACCEPTED / REAL-REQUIRED);
reason-code tokens (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT).

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite.

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.
  HALT. If any rule line is missing, write it before advancing.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  HALT. If partition does not sum to 9, recount before advancing.
  Do not proceed to STEP 3 until GATE B is written.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. DECISION SCOREBOARD applies: each namespace begins
REAL-REQUIRED. The Architect role must name a positive structural coverage argument to earn
MOCK-ACCEPTED — not merely confirm the absence of problems.

Initialize: Arch-blocked: []

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    structural variance type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — ARCHITECT PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal non-auto-flagged count from GATE B.
  HALT. If sum does not equal non-auto-flagged count, recount before advancing.

  DECISION SCOREBOARD UPDATE — after Architect phase:
  REAL-REQUIRED: ___ (auto-flagged + Arch-blocked + Strategy-pending)
  MOCK-ACCEPTED earned so far: ___ (Architect phase only; Strategy evaluation pending)

  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace (GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    domain knowledge type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE C MOCK-ACCEPTED count.
  HALT. If sum does not match, recount before advancing.

  DECISION SCOREBOARD FINAL — after Strategy phase:
  REAL-REQUIRED (final): ___ (auto-flagged + Arch-blocked + Strategy-blocked)
  MOCK-ACCEPTED (final): ___ (cleared both Architect and Strategy phases)
  CONSTRAINT: REAL-REQUIRED + MOCK-ACCEPTED must equal 9.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table with Phase as the first column:

| Phase | Namespace | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

CONSTRAINT: Each Phase cell must be exactly "Architect" or "Strategy" — matching the
  evaluation phase in which that namespace earned MOCK-ACCEPTED.
HALT. Delete any Phase cell that is not exactly "Architect" or "Strategy". Rewrite.

CONSTRAINT: Architect rows appear before Strategy rows. All Architect entries form one
  consecutive block; all Strategy entries form one consecutive block.
HALT. If rows are not grouped by phase, reorder before advancing.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Total rows confirmed: ___. Expected: ___.
  Architect rows: ___. Expected: ___ (= GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER tally at GATE C and GATE D respectively.
  HALT. If any count mismatches, identify the discrepancy against the source INERTIA LEDGER
    and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  HALT. If count is wrong, identify missing namespaces and re-run Edit for each.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  HALT. If value unchanged, the Edit call did not modify the file — output CANARY SUPPRESSED.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  HALT. If CANARY ASSERTION is missing, write it before this gate fires.
  Do not proceed to STEP 7 until GATE E is written.

---

STEP 7 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  HALT. Delete the Reason field if it is not an exact token. Rewrite with the correct token.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite.

---

STEP 8 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 9.

---

STEP 9 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status
  HALT. If any column is missing, add it before completing the Write call.

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.
  HALT. If any sentence begins with a forbidden form, rewrite it before completing the call.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.
  HALT. If Urgency column is absent, add it before completing the Write call.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.
  HALT. If any entry is missing a required field, complete it before completing the call.

---

STEP 10 — GATE F COMPLETENESS CHECK

Verify the STEP 9 Write call is complete and each section meets its structural requirement.
This step executes after the Write call returns and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Coverage table column count: ___
  CONSTRAINT: Write "4 columns confirmed: Namespace | Auto-flag | Role Verdict | Final Status"
    or "column count wrong — halt and correct before proceeding".
  HALT. If column count is wrong, correct the section and re-run the Write call before advancing.

  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Structural records sentence count: ___
  CONSTRAINT: Write "N sentences confirmed — expected 9 (one per namespace)" or
    "sentence count wrong — halt and correct before proceeding".
  HALT. If sentence count does not equal 9, correct the section and re-run before advancing.

  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Risk table Urgency column present: ___
  CONSTRAINT: Write "confirmed" or "Urgency column absent — halt and correct before proceeding".
  HALT. If Urgency column is absent, correct the section and re-run the Write call before advancing.

  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Next Steps ordered-list structure: ___
  CONSTRAINT: Write "confirmed — each entry has namespace · blocking reason · required action"
    or "list structure incomplete — halt and correct before proceeding".
  HALT. If any entry is missing a field, correct the section and re-run before advancing.

  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If filename does not match, correct it before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed with content structure verified:
    Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column / Next Steps: ordered list
  Do not claim completion until GATE F is written.

---

## V-02 — Output Format: GATE B Evaluation-Universe Enumeration

**axis:** output-format (GATE B evaluation-universe enumeration)
**hypothesis:** R9 V-05's GATE B asserts a non-flagged count but does not name which
namespaces form the evaluation set. STEP 3 must infer the evaluation universe from STEP 2
context. If the evaluation phase is long, an evaluator referencing STEP 3 can no longer
verify its scope without re-reading STEP 2. V-02 adds an explicit named-namespace list at
GATE B: after the non-flagged count, write the enumerated list of namespaces that proceed
to STEP 3 and STEP 4. This list becomes the canonical evaluation universe declaration —
STEP 3 can cite "namespaces declared in GATE B" without requiring STEP 2 re-reading. No
other steps change. All criteria from R9 V-05 preserved. Predicted score against v10: 28/28.

---

You are running /mock:accept.

DECISION SCOREBOARD
  REAL-REQUIRED: 9   (all namespaces begin here — this is inertia)
  MOCK-ACCEPTED:  0   (nothing earned yet)

MOCK-ACCEPTED is earned against named evidence. The absence of a disqualification is not
evidence. Confirmation that nothing is wrong does not move a namespace off REAL-REQUIRED.
Each earned MOCK-ACCEPTED requires a positive structural or domain argument naming what makes
real data unnecessary for that namespace at this tier.

This scoreboard governs STEP 3 (Architect phase) and STEP 4 (Strategy phase).
GATE C records the Architect phase movement. GATE D records the Strategy phase movement.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

Exempt from this rule: tier sourcing output (Tier: N (source: …)); auto-flag Rule A/B/C
definition headers; verdict tokens used as classifiers (MOCK-ACCEPTED / REAL-REQUIRED);
reason-code tokens (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT).

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite.

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.
  HALT. If any rule line is missing, write it before advancing.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  HALT. If partition does not sum to 9, recount before advancing.
  Evaluation universe: ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list. This list is the canonical
    scope for STEP 3 and STEP 4. An anonymous count alone does not satisfy.
  HALT. If the evaluation universe list is absent or incomplete, write it before advancing.
  Do not proceed to STEP 3 until GATE B is written with evaluation universe list.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. DECISION SCOREBOARD applies: each namespace begins
REAL-REQUIRED. The Architect role must name a positive structural coverage argument to earn
MOCK-ACCEPTED — not merely confirm the absence of problems.

Initialize: Arch-blocked: []

For each namespace in the GATE B evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    structural variance type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE B evaluation universe count. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — ARCHITECT PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE B evaluation universe count.
  HALT. If sum does not equal that count, recount before advancing.

  DECISION SCOREBOARD UPDATE — after Architect phase:
  REAL-REQUIRED: ___ (auto-flagged + Arch-blocked + Strategy-pending)
  MOCK-ACCEPTED earned so far: ___ (Architect phase only; Strategy evaluation pending)

  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace (GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    domain knowledge type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE C MOCK-ACCEPTED count.
  HALT. If sum does not match, recount before advancing.

  DECISION SCOREBOARD FINAL — after Strategy phase:
  REAL-REQUIRED (final): ___ (auto-flagged + Arch-blocked + Strategy-blocked)
  MOCK-ACCEPTED (final): ___ (cleared both Architect and Strategy phases)
  CONSTRAINT: REAL-REQUIRED + MOCK-ACCEPTED must equal 9.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table with Phase as the first column:

| Phase | Namespace | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

CONSTRAINT: Each Phase cell must be exactly "Architect" or "Strategy" — matching the
  evaluation phase in which that namespace earned MOCK-ACCEPTED.
HALT. Delete any Phase cell that is not exactly "Architect" or "Strategy". Rewrite.

CONSTRAINT: Architect rows appear before Strategy rows. All Architect entries form one
  consecutive block; all Strategy entries form one consecutive block.
HALT. If rows are not grouped by phase, reorder before advancing.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Total rows confirmed: ___. Expected: ___.
  Architect rows: ___. Expected: ___ (= GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER tally at GATE C and GATE D respectively.
  HALT. If any count mismatches, identify the discrepancy against the source INERTIA LEDGER
    and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  HALT. If count is wrong, identify missing namespaces and re-run Edit for each.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  HALT. If value unchanged, the Edit call did not modify the file — output CANARY SUPPRESSED.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  HALT. If CANARY ASSERTION is missing, write it before this gate fires.
  Do not proceed to STEP 7 until GATE E is written.

---

STEP 7 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  HALT. Delete the Reason field if it is not an exact token. Rewrite with the correct token.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite.

---

STEP 8 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 9.

---

STEP 9 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status
  HALT. If any column is missing, add it before completing the Write call.

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.
  HALT. If any sentence begins with a forbidden form, rewrite it before completing the call.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.
  HALT. If Urgency column is absent, add it before completing the Write call.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.
  HALT. If any entry is missing a required field, complete it before completing the call.

---

STEP 10 — GATE F COMPLETENESS CHECK

Verify the STEP 9 Write call is complete. This step executes after the Write call returns
and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If filename does not match, correct it before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed: Coverage / Structural records / Risk / Next Steps
  Do not claim completion until GATE F is written.

---

## V-03 — Role Sequence: ROLE HANDOFF Declaration

**axis:** role-sequence (ROLE HANDOFF block between GATE C and STEP 4)
**hypothesis:** R9 V-05 marks the Architect-to-Strategy transition with GATE C's "Do not
proceed to STEP 4 until GATE C is written" language. STEP 4 says "For each Architect-ACCEPTED
namespace (GATE C)" — referencing the gate, not a written list. An evaluator beginning STEP 4
must scan back to GATE C's INERTIA LEDGER to reconstruct the Strategy evaluation universe.
V-03 adds a named ROLE HANDOFF block between GATE C and STEP 4 that explicitly enumerates
the namespaces entering the Strategy phase. The ROLE HANDOFF closes the Architect phase as a
named event and opens the Strategy phase with a declared scope — STEP 4 cites the ROLE HANDOFF
list, not the GATE C INERTIA LEDGER, as its universe source. All other steps identical to R9
V-05. Predicted score against v10: 28/28.

---

You are running /mock:accept.

DECISION SCOREBOARD
  REAL-REQUIRED: 9   (all namespaces begin here — this is inertia)
  MOCK-ACCEPTED:  0   (nothing earned yet)

MOCK-ACCEPTED is earned against named evidence. The absence of a disqualification is not
evidence. Confirmation that nothing is wrong does not move a namespace off REAL-REQUIRED.
Each earned MOCK-ACCEPTED requires a positive structural or domain argument naming what makes
real data unnecessary for that namespace at this tier.

This scoreboard governs STEP 3 (Architect phase) and STEP 4 (Strategy phase).
GATE C records the Architect phase movement. GATE D records the Strategy phase movement.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

Exempt from this rule: tier sourcing output (Tier: N (source: …)); auto-flag Rule A/B/C
definition headers; verdict tokens used as classifiers (MOCK-ACCEPTED / REAL-REQUIRED);
reason-code tokens (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT).

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite.

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.
  HALT. If any rule line is missing, write it before advancing.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  HALT. If partition does not sum to 9, recount before advancing.
  Do not proceed to STEP 3 until GATE B is written.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. DECISION SCOREBOARD applies: each namespace begins
REAL-REQUIRED. The Architect role must name a positive structural coverage argument to earn
MOCK-ACCEPTED — not merely confirm the absence of problems.

Initialize: Arch-blocked: []

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    structural variance type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — ARCHITECT PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal non-auto-flagged count from GATE B.
  HALT. If sum does not equal non-auto-flagged count, recount before advancing.

  DECISION SCOREBOARD UPDATE — after Architect phase:
  REAL-REQUIRED: ___ (auto-flagged + Arch-blocked + Strategy-pending)
  MOCK-ACCEPTED earned so far: ___ (Architect phase only; Strategy evaluation pending)

  Do not proceed to STEP 4 until GATE C is written.

---

ROLE HANDOFF — Architect Phase Closed / Strategy Phase Opens

  Strategy evaluation universe: ___
  CONSTRAINT: Name each namespace from the GATE C INERTIA LEDGER "earned MOCK-ACCEPTED"
    list explicitly. These are the only namespaces that enter STEP 4.
  HALT. If this list is not written before STEP 4 begins, write it now.
  CONSTRAINT: Count must equal GATE C MOCK-ACCEPTED count.
  HALT. If count does not match GATE C MOCK-ACCEPTED, reconcile before advancing.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Namespaces declared in ROLE HANDOFF only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each namespace in the ROLE HANDOFF list, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    domain knowledge type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal ROLE HANDOFF count.
  HALT. If sum does not match, recount before advancing.

  DECISION SCOREBOARD FINAL — after Strategy phase:
  REAL-REQUIRED (final): ___ (auto-flagged + Arch-blocked + Strategy-blocked)
  MOCK-ACCEPTED (final): ___ (cleared both Architect and Strategy phases)
  CONSTRAINT: REAL-REQUIRED + MOCK-ACCEPTED must equal 9.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table with Phase as the first column:

| Phase | Namespace | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

CONSTRAINT: Each Phase cell must be exactly "Architect" or "Strategy" — matching the
  evaluation phase in which that namespace earned MOCK-ACCEPTED.
HALT. Delete any Phase cell that is not exactly "Architect" or "Strategy". Rewrite.

CONSTRAINT: Architect rows appear before Strategy rows. All Architect entries form one
  consecutive block; all Strategy entries form one consecutive block.
HALT. If rows are not grouped by phase, reorder before advancing.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Total rows confirmed: ___. Expected: ___.
  Architect rows: ___. Expected: ___ (= GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER tally at GATE C and GATE D respectively.
  HALT. If any count mismatches, identify the discrepancy against the source INERTIA LEDGER
    and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  HALT. If count is wrong, identify missing namespaces and re-run Edit for each.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  HALT. If value unchanged, the Edit call did not modify the file — output CANARY SUPPRESSED.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  HALT. If CANARY ASSERTION is missing, write it before this gate fires.
  Do not proceed to STEP 7 until GATE E is written.

---

STEP 7 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  HALT. Delete the Reason field if it is not an exact token. Rewrite with the correct token.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite.

---

STEP 8 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 9.

---

STEP 9 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status
  HALT. If any column is missing, add it before completing the Write call.

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.
  HALT. If any sentence begins with a forbidden form, rewrite it before completing the call.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.
  HALT. If Urgency column is absent, add it before completing the Write call.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.
  HALT. If any entry is missing a required field, complete it before completing the call.

---

STEP 10 — GATE F COMPLETENESS CHECK

Verify the STEP 9 Write call is complete. This step executes after the Write call returns
and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If filename does not match, correct it before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed: Coverage / Structural records / Risk / Next Steps
  Do not claim completion until GATE F is written.

---

## V-04 — Combined: GATE F Content Verification + GATE B Evaluation-Universe Enumeration

**axis:** combined (V-01 GATE F content verification + V-02 GATE B evaluation-universe enumeration)
**hypothesis:** V-01 adds per-section content assertions inside GATE F, making it a
content-completeness gate. V-02 adds an explicit named-namespace list at GATE B, making the
evaluation universe independently verifiable. Together: GATE B declares which namespaces enter
evaluation (independently verifiable scope); GATE F verifies not just that each section exists
but that its content meets structural requirements (independently verifiable completeness). Both
gates upgrade from assertion-by-count to assertion-by-structure. All other steps identical to
R9 V-05. Predicted score against v10: 28/28.

---

You are running /mock:accept.

DECISION SCOREBOARD
  REAL-REQUIRED: 9   (all namespaces begin here — this is inertia)
  MOCK-ACCEPTED:  0   (nothing earned yet)

MOCK-ACCEPTED is earned against named evidence. The absence of a disqualification is not
evidence. Confirmation that nothing is wrong does not move a namespace off REAL-REQUIRED.
Each earned MOCK-ACCEPTED requires a positive structural or domain argument naming what makes
real data unnecessary for that namespace at this tier.

This scoreboard governs STEP 3 (Architect phase) and STEP 4 (Strategy phase).
GATE C records the Architect phase movement. GATE D records the Strategy phase movement.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

Exempt from this rule: tier sourcing output (Tier: N (source: …)); auto-flag Rule A/B/C
definition headers; verdict tokens used as classifiers (MOCK-ACCEPTED / REAL-REQUIRED);
reason-code tokens (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT).

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite.

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.
  HALT. If any rule line is missing, write it before advancing.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  HALT. If partition does not sum to 9, recount before advancing.
  Evaluation universe: ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list. This list is the canonical
    scope for STEP 3 and STEP 4. An anonymous count alone does not satisfy.
  HALT. If the evaluation universe list is absent or incomplete, write it before advancing.
  Do not proceed to STEP 3 until GATE B is written with evaluation universe list.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. DECISION SCOREBOARD applies: each namespace begins
REAL-REQUIRED. The Architect role must name a positive structural coverage argument to earn
MOCK-ACCEPTED — not merely confirm the absence of problems.

Initialize: Arch-blocked: []

For each namespace in the GATE B evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    structural variance type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE B evaluation universe count. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — ARCHITECT PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE B evaluation universe count.
  HALT. If sum does not equal that count, recount before advancing.

  DECISION SCOREBOARD UPDATE — after Architect phase:
  REAL-REQUIRED: ___ (auto-flagged + Arch-blocked + Strategy-pending)
  MOCK-ACCEPTED earned so far: ___ (Architect phase only; Strategy evaluation pending)

  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace (GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    domain knowledge type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE C MOCK-ACCEPTED count.
  HALT. If sum does not match, recount before advancing.

  DECISION SCOREBOARD FINAL — after Strategy phase:
  REAL-REQUIRED (final): ___ (auto-flagged + Arch-blocked + Strategy-blocked)
  MOCK-ACCEPTED (final): ___ (cleared both Architect and Strategy phases)
  CONSTRAINT: REAL-REQUIRED + MOCK-ACCEPTED must equal 9.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table with Phase as the first column:

| Phase | Namespace | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

CONSTRAINT: Each Phase cell must be exactly "Architect" or "Strategy" — matching the
  evaluation phase in which that namespace earned MOCK-ACCEPTED.
HALT. Delete any Phase cell that is not exactly "Architect" or "Strategy". Rewrite.

CONSTRAINT: Architect rows appear before Strategy rows. All Architect entries form one
  consecutive block; all Strategy entries form one consecutive block.
HALT. If rows are not grouped by phase, reorder before advancing.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Total rows confirmed: ___. Expected: ___.
  Architect rows: ___. Expected: ___ (= GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER tally at GATE C and GATE D respectively.
  HALT. If any count mismatches, identify the discrepancy against the source INERTIA LEDGER
    and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  HALT. If count is wrong, identify missing namespaces and re-run Edit for each.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  HALT. If value unchanged, the Edit call did not modify the file — output CANARY SUPPRESSED.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  HALT. If CANARY ASSERTION is missing, write it before this gate fires.
  Do not proceed to STEP 7 until GATE E is written.

---

STEP 7 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  HALT. Delete the Reason field if it is not an exact token. Rewrite with the correct token.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite.

---

STEP 8 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 9.

---

STEP 9 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status
  HALT. If any column is missing, add it before completing the Write call.

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.
  HALT. If any sentence begins with a forbidden form, rewrite it before completing the call.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.
  HALT. If Urgency column is absent, add it before completing the Write call.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.
  HALT. If any entry is missing a required field, complete it before completing the call.

---

STEP 10 — GATE F COMPLETENESS CHECK

Verify the STEP 9 Write call is complete and each section meets its structural requirement.
This step executes after the Write call returns and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Coverage table column count: ___
  CONSTRAINT: Write "4 columns confirmed: Namespace | Auto-flag | Role Verdict | Final Status"
    or "column count wrong — halt and correct before proceeding".
  HALT. If column count is wrong, correct the section and re-run the Write call before advancing.

  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Structural records sentence count: ___
  CONSTRAINT: Write "N sentences confirmed — expected 9 (one per namespace)" or
    "sentence count wrong — halt and correct before proceeding".
  HALT. If sentence count does not equal 9, correct the section and re-run before advancing.

  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Risk table Urgency column present: ___
  CONSTRAINT: Write "confirmed" or "Urgency column absent — halt and correct before proceeding".
  HALT. If Urgency column is absent, correct the section and re-run the Write call before advancing.

  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Next Steps ordered-list structure: ___
  CONSTRAINT: Write "confirmed — each entry has namespace · blocking reason · required action"
    or "list structure incomplete — halt and correct before proceeding".
  HALT. If any entry is missing a field, correct the section and re-run before advancing.

  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If filename does not match, correct it before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed with content structure verified:
    Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column / Next Steps: ordered list
  Do not claim completion until GATE F is written.

---

## V-05 — Combined: GATE F Content + GATE B Enumeration + ROLE HANDOFF

**axis:** combined (V-01 + V-02 + V-03)
**hypothesis:** V-01 adds per-section content assertions to GATE F. V-02 adds the evaluation
universe list to GATE B. V-03 adds a ROLE HANDOFF block between GATE C and STEP 4 that names
the Strategy phase universe. Together: GATE B declares scope before evaluation begins (V-02);
GATE C closes Architect phase and a ROLE HANDOFF block opens Strategy phase with an enumerated
scope (V-03); GATE F verifies each review artifact section by content structure, not presence
only (V-01). Three scope-declaration events — GATE B universe, ROLE HANDOFF universe, GATE F
content assertions — each independently verifiable without cross-phase re-reading. All 28
v10 criteria preserved. Predicted score against v10: 28/28.

---

You are running /mock:accept.

DECISION SCOREBOARD
  REAL-REQUIRED: 9   (all namespaces begin here — this is inertia)
  MOCK-ACCEPTED:  0   (nothing earned yet)

MOCK-ACCEPTED is earned against named evidence. The absence of a disqualification is not
evidence. Confirmation that nothing is wrong does not move a namespace off REAL-REQUIRED.
Each earned MOCK-ACCEPTED requires a positive structural or domain argument naming what makes
real data unnecessary for that namespace at this tier.

This scoreboard governs STEP 3 (Architect phase) and STEP 4 (Strategy phase).
GATE C records the Architect phase movement. GATE D records the Strategy phase movement.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

Exempt from this rule: tier sourcing output (Tier: N (source: …)); auto-flag Rule A/B/C
definition headers; verdict tokens used as classifiers (MOCK-ACCEPTED / REAL-REQUIRED);
reason-code tokens (STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT).

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite.

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.
  HALT. If any rule line is missing, write it before advancing.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  HALT. If partition does not sum to 9, recount before advancing.
  Evaluation universe: ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list. This list is the canonical
    scope for STEP 3 and STEP 4. An anonymous count alone does not satisfy.
  HALT. If the evaluation universe list is absent or incomplete, write it before advancing.
  Do not proceed to STEP 3 until GATE B is written with evaluation universe list.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. DECISION SCOREBOARD applies: each namespace begins
REAL-REQUIRED. The Architect role must name a positive structural coverage argument to earn
MOCK-ACCEPTED — not merely confirm the absence of problems.

Initialize: Arch-blocked: []

For each namespace in the GATE B evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    structural variance type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE B evaluation universe count. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — ARCHITECT PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE B evaluation universe count.
  HALT. If sum does not equal that count, recount before advancing.

  DECISION SCOREBOARD UPDATE — after Architect phase:
  REAL-REQUIRED: ___ (auto-flagged + Arch-blocked + Strategy-pending)
  MOCK-ACCEPTED earned so far: ___ (Architect phase only; Strategy evaluation pending)

  Do not proceed to STEP 4 until GATE C is written.

---

ROLE HANDOFF — Architect Phase Closed / Strategy Phase Opens

  Strategy evaluation universe: ___
  CONSTRAINT: Name each namespace from the GATE C INERTIA LEDGER "earned MOCK-ACCEPTED"
    list explicitly. These are the only namespaces that enter STEP 4.
  HALT. If this list is not written before STEP 4 begins, write it now.
  CONSTRAINT: Count must equal GATE C MOCK-ACCEPTED count.
  HALT. If count does not match GATE C MOCK-ACCEPTED, reconcile before advancing.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Namespaces declared in ROLE HANDOFF only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each namespace in the ROLE HANDOFF list, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  HALT. Delete Artifact state if it contains a forbidden form. Rewrite in PASS form.
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Verdict if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.
  Cost-of-MOCK: ___
  CONSTRAINT: If Verdict is MOCK-ACCEPTED, write "Without real data for [namespace], [specific
    domain knowledge type] remains unvalidated by production evidence at Tier [N]." If
    Verdict is REAL-REQUIRED, write "N/A".
  HALT. Delete Cost-of-MOCK if it does not match the required format. Rewrite.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal ROLE HANDOFF count.
  HALT. If sum does not match, recount before advancing.

  DECISION SCOREBOARD FINAL — after Strategy phase:
  REAL-REQUIRED (final): ___ (auto-flagged + Arch-blocked + Strategy-blocked)
  MOCK-ACCEPTED (final): ___ (cleared both Architect and Strategy phases)
  CONSTRAINT: REAL-REQUIRED + MOCK-ACCEPTED must equal 9.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table with Phase as the first column:

| Phase | Namespace | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

CONSTRAINT: Each Phase cell must be exactly "Architect" or "Strategy" — matching the
  evaluation phase in which that namespace earned MOCK-ACCEPTED.
HALT. Delete any Phase cell that is not exactly "Architect" or "Strategy". Rewrite.

CONSTRAINT: Architect rows appear before Strategy rows. All Architect entries form one
  consecutive block; all Strategy entries form one consecutive block.
HALT. If rows are not grouped by phase, reorder before advancing.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Total rows confirmed: ___. Expected: ___.
  Architect rows: ___. Expected: ___ (= GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER "earned MOCK-ACCEPTED" count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER tally at GATE C and GATE D respectively.
  HALT. If any count mismatches, identify the discrepancy against the source INERTIA LEDGER
    and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  HALT. If count is wrong, identify missing namespaces and re-run Edit for each.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  HALT. If value unchanged, the Edit call did not modify the file — output CANARY SUPPRESSED.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  HALT. If CANARY ASSERTION is missing, write it before this gate fires.
  Do not proceed to STEP 7 until GATE E is written.

---

STEP 7 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  HALT. Delete the Reason field if it is not an exact token. Rewrite with the correct token.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite.

---

STEP 8 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 9.

---

STEP 9 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status
  HALT. If any column is missing, add it before completing the Write call.

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.
  HALT. If any sentence begins with a forbidden form, rewrite it before completing the call.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.
  HALT. If Urgency column is absent, add it before completing the Write call.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.
  HALT. If any entry is missing a required field, complete it before completing the call.

---

STEP 10 — GATE F COMPLETENESS CHECK

Verify the STEP 9 Write call is complete and each section meets its structural requirement.
This step executes after the Write call returns and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Coverage table column count: ___
  CONSTRAINT: Write "4 columns confirmed: Namespace | Auto-flag | Role Verdict | Final Status"
    or "column count wrong — halt and correct before proceeding".
  HALT. If column count is wrong, correct the section and re-run the Write call before advancing.

  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Structural records sentence count: ___
  CONSTRAINT: Write "N sentences confirmed — expected 9 (one per namespace)" or
    "sentence count wrong — halt and correct before proceeding".
  HALT. If sentence count does not equal 9, correct the section and re-run before advancing.

  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Risk table Urgency column present: ___
  CONSTRAINT: Write "confirmed" or "Urgency column absent — halt and correct before proceeding".
  HALT. If Urgency column is absent, correct the section and re-run the Write call before advancing.

  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  HALT. If absent, add the missing section and re-run the Write call before advancing.
  Next Steps ordered-list structure: ___
  CONSTRAINT: Write "confirmed — each entry has namespace · blocking reason · required action"
    or "list structure incomplete — halt and correct before proceeding".
  HALT. If any entry is missing a field, correct the section and re-run before advancing.

  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If filename does not match, correct it before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed with content structure verified:
    Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column / Next Steps: ordered list
  Do not claim completion until GATE F is written.
