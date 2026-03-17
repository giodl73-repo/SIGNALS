---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 11
rubric_version: v11
status: VARIATE
---

# mock-accept Variate — Round 11

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v11 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-39 aspirational;
             C-37/C-38/C-39 new this round; denominator 31)
**Baseline:** R10 V-05 (sole golden, 31/31 against v11: GATE F section format qualifiers +
             GATE B evaluation-universe enumeration + ROLE HANDOFF block)
**Round:** R11 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R10 V-05 is the sole golden at 31/31 against v11. The three R10 criteria
(C-37/C-38/C-39) tightened verifiability at GATE F (section structure), GATE B
(partition membership), and the Architect-to-Strategy boundary (ROLE HANDOFF). R11
probes three structural questions that v11's golden leaves open:

1. The ROLE HANDOFF (C-39) satisfies by naming the Strategy evaluation universe —
   who enters STEP 4. The inverse — who was closed as REAL-REQUIRED in the Architect
   phase — is implicit in GATE C's Arch-blocked list but not restated at the handoff
   boundary. Does a bidirectional ROLE HANDOFF (entering set + closed set + live
   SCOREBOARD values) make the phase boundary a complete and independently verifiable
   partition record, without requiring GATE C re-reading?

2. C-38's GATE B enumeration names the non-flagged evaluation universe but leaves the
   auto-flagged bucket as a count. The three logical buckets are: auto-flagged /
   Architect-phase / Strategy-phase. Does enumerating all three buckets at GATE B —
   including naming each auto-flagged namespace under its own bucket — make GATE B a
   complete three-way partition record rather than a count plus partial enumeration?

3. GATE D's INERTIA LEDGER reports total MOCK-ACCEPTED at Strategy phase exit but does
   not distinguish earners by phase (Architect vs Strategy). The COST REGISTER (STEP 5)
   makes this split explicit, but GATE D does not require phase attribution before the
   COST REGISTER runs. Does adding phase-attributed sub-lists inside the GATE D
   INERTIA LEDGER create an independent pre-STEP-5 verification layer for the
   Architect/Strategy MOCK-ACCEPTED split?

| Plan | Axis | Target | What changes from R10 V-05 | Predicted |
|------|------|--------|---------------------------|-----------|
| V-01 | role-sequence / inertia-framing (bidirectional ROLE HANDOFF) | ROLE HANDOFF block | ROLE HANDOFF adds closed-set enumeration (Arch-blocked names) + SCOREBOARD state + full partition check alongside entering-set enumeration | 31/31 |
| V-02 | output-format (GATE B three-bucket named partition) | GATE B | GATE B adds auto-flagged named list completing full three-bucket enumeration; all three buckets named, not just evaluation universe | 31/31 |
| V-03 | lifecycle-emphasis (GATE D phase-attributed INERTIA LEDGER) | GATE D INERTIA LEDGER | GATE D INERTIA LEDGER adds phase-attributed sub-lists (Architect-earners / Strategy-earners) with count constraints against GATE C and GATE D MOCK-ACCEPTED | 31/31 |
| V-04 | combined: bidirectional ROLE HANDOFF + GATE B three-bucket | V-01 + V-02 | Full bidirectional ROLE HANDOFF + complete three-bucket GATE B partition | 31/31 |
| V-05 | combined: all three | V-01 + V-02 + V-03 | Bidirectional ROLE HANDOFF + three-bucket GATE B + phase-attributed GATE D | 31/31 |

---

## V-01 — Inertia Framing: ROLE HANDOFF Bidirectional State Capture

**axis:** role-sequence / inertia-framing (ROLE HANDOFF bidirectional state capture)
**hypothesis:** R10 V-05's ROLE HANDOFF names the Strategy evaluation universe — the
namespaces that cleared Architect phase and enter STEP 4. C-39 is satisfied. But the
handoff carries only one direction of state: who enters. The closed set — namespaces
that did not clear Architect phase and are now permanently at REAL-REQUIRED — is
implicit in GATE C's Arch-blocked list just above the handoff, but it is not restated
at the boundary. An evaluator entering STEP 4 can reconstruct the partition by reading
GATE C, but the handoff block itself is not self-contained. V-01 expands the ROLE
HANDOFF to a full bidirectional state transfer: (1) DECISION SCOREBOARD values copied
from GATE C UPDATE, (2) Arch-blocked names (closed at REAL-REQUIRED), (3) Strategy
evaluation universe names (entering STEP 4), (4) a partition sum check confirming
blocked + entering = GATE B non-flagged count. The ROLE HANDOFF becomes independently
auditable at the phase boundary without requiring GATE C re-reading. All other steps
identical to R10 V-05. Predicted score against v11: 31/31.

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

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]..."
  FAIL forms: "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..."

Exempt from this rule: tier sourcing output (Tier: N (source: ...)); auto-flag Rule A/B/C
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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Arch-blocked: [namespace] added."
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

  Do not proceed to ROLE HANDOFF until GATE C is written.

---

ROLE HANDOFF — Architect Phase Closed / Strategy Phase Opens

  DECISION SCOREBOARD at handoff:
  REAL-REQUIRED: ___ / MOCK-ACCEPTED: ___
  CONSTRAINT: Copy values from GATE C DECISION SCOREBOARD UPDATE verbatim.
  HALT. If values are absent or do not match GATE C UPDATE exactly, rewrite before advancing.

  INERTIA LEDGER at handoff:
  Arch-blocked (closed as REAL-REQUIRED): ___
  CONSTRAINT: Name each Arch-blocked namespace explicitly. List must match GATE C
    INERTIA LEDGER "Namespaces still at REAL-REQUIRED default" exactly.
  HALT. If Arch-blocked list is absent or any name mismatches GATE C, rewrite before advancing.

  Strategy evaluation universe (entering STEP 4): ___
  CONSTRAINT: Name each namespace from GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" list
    explicitly. These are the only namespaces that enter STEP 4.
  HALT. If this list is absent or any name mismatches GATE C, write it before advancing.

  Partition check: ___ Arch-blocked + ___ entering STEP 4 = ___
  CONSTRAINT: Sum must equal GATE B non-flagged count. Both sets together account for the
    complete evaluation universe — no namespace is unassigned at this boundary.
  HALT. If sum does not equal GATE B non-flagged count, reconcile before advancing.

  Do not begin STEP 4 until ROLE HANDOFF is written with all four fields.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Namespaces declared in ROLE HANDOFF only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each namespace in the ROLE HANDOFF Strategy evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF entering count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal ROLE HANDOFF entering count.
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
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for..."
HALT. If any cell does not begin "Without real data for...", replace it with the verbatim
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
  auto-flagged (GATE B) -> REAL-REQUIRED
  Arch-blocked (GATE C) -> REAL-REQUIRED
  Strategy-blocked (GATE D) -> REAL-REQUIRED
  all others -> MOCK-ACCEPTED

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section..." — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers..." | evaluator-subject form |
  | "Coverage demonstrates that..." | evaluator-subject form |
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

## V-02 — Output Format: GATE B Three-Bucket Named Partition

**axis:** output-format (GATE B three-bucket named partition)
**hypothesis:** R10 V-05's GATE B satisfies C-38 by naming each non-flagged namespace
under the evaluation universe bucket. The auto-flagged bucket is reported as a count
only — the individual auto-flagged namespace names appear in STEP 2's Rule A/B/C
outputs but are not re-enumerated at GATE B under a named bucket. The three logical
partition buckets are: auto-flagged / Architect-phase / Strategy-phase. C-38 requires
each namespace named within its bucket. V-02 interprets C-38 strictly: GATE B must
enumerate all three buckets by name, including listing each auto-flagged namespace
under an "Auto-flagged" sub-list. With this change GATE B becomes a complete three-way
partition record — all 9 namespaces appear at GATE B, each under exactly one named
bucket, and the complete partition is auditable at GATE B without reading STEP 2 or
the evaluation records. All other steps identical to R10 V-05. Predicted score
against v11: 31/31.

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

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]..."
  FAIL forms: "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..."

Exempt from this rule: tier sourcing output (Tier: N (source: ...)); auto-flag Rule A/B/C
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
  CONSTRAINT: Total flags count. Verify sum before writing partition.
  HALT. If total is inconsistent with Rule A/B/C counts, recount before advancing.

  Partition:

  Auto-flagged bucket: ___
  CONSTRAINT: Name each auto-flagged namespace explicitly as a list under this bucket.
    Count must equal total flags above. Write "Auto-flagged: none" if count is 0.
  HALT. If auto-flagged list is absent or count mismatches total flags, write it before advancing.

  Evaluation universe bucket (Architect-phase + Strategy-phase): ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list under this bucket.
    Count must equal 9 - total flags. This list is the canonical scope for STEP 3 and STEP 4.
    An anonymous count alone does not satisfy.
  HALT. If evaluation universe list is absent or incomplete, write it before advancing.

  Partition check: ___ auto-flagged + ___ evaluation universe = ___
  CONSTRAINT: Sum must equal 9. All three bucket fields required before advancing.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 3 until GATE B is written with both named bucket lists.

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Arch-blocked: [namespace] added."
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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Strategy-blocked: [namespace] added."
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
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for..."
HALT. If any cell does not begin "Without real data for...", replace it with the verbatim
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
  auto-flagged (GATE B) -> REAL-REQUIRED
  Arch-blocked (GATE C) -> REAL-REQUIRED
  Strategy-blocked (GATE D) -> REAL-REQUIRED
  all others -> MOCK-ACCEPTED

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section..." — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers..." | evaluator-subject form |
  | "Coverage demonstrates that..." | evaluator-subject form |
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

## V-03 — Lifecycle Emphasis: GATE D Phase-Attributed INERTIA LEDGER

**axis:** lifecycle-emphasis (GATE D phase-attributed INERTIA LEDGER)
**hypothesis:** R10 V-05's GATE D INERTIA LEDGER reports a single total for
"Namespaces that have earned MOCK-ACCEPTED against inertia" without distinguishing
earners from the Architect phase from earners from the Strategy phase. The COST
REGISTER (STEP 5) makes this split explicit via the Phase column (C-33/C-34). But
GATE D does not require the evaluator to state the phase attribution before STEP 5
runs — the attribution is derivable from GATE C and GATE D counts, but it is not
a required written assertion at the Strategy phase boundary. V-03 adds phase-attributed
sub-lists inside the GATE D INERTIA LEDGER: "Architect-phase earners: [list]" and
"Strategy-phase earners: [list]", each with count constraints against GATE C and this
gate's MOCK-ACCEPTED respectively. The phase-attributed INERTIA LEDGER at GATE D
becomes an independent pre-STEP-5 verification layer — the Architect/Strategy
MOCK-ACCEPTED split is asserted and HALT-blocked before the COST REGISTER begins,
not merely verifiable by COST REGISTER inspection afterward. All other steps identical
to R10 V-05. Predicted score against v11: 31/31.

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

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]..."
  FAIL forms: "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..."

Exempt from this rule: tier sourcing output (Tier: N (source: ...)); auto-flag Rule A/B/C
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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Arch-blocked: [namespace] added."
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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default (Strategy-blocked): ___
  Namespaces that have earned MOCK-ACCEPTED against inertia — by phase:

    Architect-phase earners: ___
    CONSTRAINT: Names must match GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" list exactly.
      Count must equal GATE C MOCK-ACCEPTED count.
    HALT. If list is absent or any name mismatches GATE C INERTIA LEDGER, rewrite before advancing.

    Strategy-phase earners: ___
    CONSTRAINT: Names must match this gate's MOCK-ACCEPTED count above (namespaces that earned
      MOCK-ACCEPTED in STEP 4). Write "Strategy-phase earners: none" if count is 0.
    HALT. If list is absent or count mismatches this gate's MOCK-ACCEPTED, rewrite before advancing.

  Total MOCK-ACCEPTED: ___
  CONSTRAINT: Architect-phase earner count + Strategy-phase earner count = Total MOCK-ACCEPTED.
    Total MOCK-ACCEPTED + Strategy-blocked count = ROLE HANDOFF entering count.
  HALT. If either constraint fails, reconcile before advancing.

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
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for..."
HALT. If any cell does not begin "Without real data for...", replace it with the verbatim
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
  Architect rows: ___. Expected: ___ (= GATE D INERTIA LEDGER Architect-phase earner count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER Strategy-phase earner count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER phase-earner tally at GATE D.
  HALT. If any count mismatches, identify the discrepancy against the GATE D phase-earner
    lists and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) -> REAL-REQUIRED
  Arch-blocked (GATE C) -> REAL-REQUIRED
  Strategy-blocked (GATE D) -> REAL-REQUIRED
  all others -> MOCK-ACCEPTED

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section..." — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers..." | evaluator-subject form |
  | "Coverage demonstrates that..." | evaluator-subject form |
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

## V-04 — Combined: Bidirectional ROLE HANDOFF + GATE B Three-Bucket Partition

**axis:** combined (V-01 bidirectional ROLE HANDOFF + V-02 GATE B three-bucket named partition)
**hypothesis:** V-01 expands the ROLE HANDOFF to carry both directions of phase state:
who enters STEP 4 and who was closed as REAL-REQUIRED in the Architect phase, with a
SCOREBOARD snapshot and partition sum check. V-02 completes GATE B's partition record
by enumerating all three buckets including the auto-flagged namespace names. Together:
GATE B is a complete three-way partition record (all 9 namespaces named under one of
three buckets); the ROLE HANDOFF is a complete bidirectional boundary record (entering
+ closed + SCOREBOARD state). Both gates upgrade from partial enumeration to full
enumeration. All other steps identical to R10 V-05. Predicted score against v11: 31/31.

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

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]..."
  FAIL forms: "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..."

Exempt from this rule: tier sourcing output (Tier: N (source: ...)); auto-flag Rule A/B/C
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
  CONSTRAINT: Total flags count. Verify sum before writing partition.
  HALT. If total is inconsistent with Rule A/B/C counts, recount before advancing.

  Partition:

  Auto-flagged bucket: ___
  CONSTRAINT: Name each auto-flagged namespace explicitly as a list under this bucket.
    Count must equal total flags above. Write "Auto-flagged: none" if count is 0.
  HALT. If auto-flagged list is absent or count mismatches total flags, write it before advancing.

  Evaluation universe bucket (Architect-phase + Strategy-phase): ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list under this bucket.
    Count must equal 9 - total flags. This list is the canonical scope for STEP 3 and STEP 4.
    An anonymous count alone does not satisfy.
  HALT. If evaluation universe list is absent or incomplete, write it before advancing.

  Partition check: ___ auto-flagged + ___ evaluation universe = ___
  CONSTRAINT: Sum must equal 9. All three bucket fields required before advancing.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 3 until GATE B is written with both named bucket lists.

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Arch-blocked: [namespace] added."
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

  Do not proceed to ROLE HANDOFF until GATE C is written.

---

ROLE HANDOFF — Architect Phase Closed / Strategy Phase Opens

  DECISION SCOREBOARD at handoff:
  REAL-REQUIRED: ___ / MOCK-ACCEPTED: ___
  CONSTRAINT: Copy values from GATE C DECISION SCOREBOARD UPDATE verbatim.
  HALT. If values are absent or do not match GATE C UPDATE exactly, rewrite before advancing.

  INERTIA LEDGER at handoff:
  Arch-blocked (closed as REAL-REQUIRED): ___
  CONSTRAINT: Name each Arch-blocked namespace explicitly. List must match GATE C
    INERTIA LEDGER "Namespaces still at REAL-REQUIRED default" exactly.
  HALT. If Arch-blocked list is absent or any name mismatches GATE C, rewrite before advancing.

  Strategy evaluation universe (entering STEP 4): ___
  CONSTRAINT: Name each namespace from GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" list
    explicitly. These are the only namespaces that enter STEP 4.
  HALT. If this list is absent or any name mismatches GATE C, write it before advancing.

  Partition check: ___ Arch-blocked + ___ entering STEP 4 = ___
  CONSTRAINT: Sum must equal GATE B evaluation universe count. Both sets together account for
    the complete evaluation universe — no namespace is unassigned at this boundary.
  HALT. If sum does not equal GATE B evaluation universe count, reconcile before advancing.

  Do not begin STEP 4 until ROLE HANDOFF is written with all four fields.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Namespaces declared in ROLE HANDOFF only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each namespace in the ROLE HANDOFF Strategy evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF entering count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal ROLE HANDOFF entering count.
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
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for..."
HALT. If any cell does not begin "Without real data for...", replace it with the verbatim
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
  auto-flagged (GATE B) -> REAL-REQUIRED
  Arch-blocked (GATE C) -> REAL-REQUIRED
  Strategy-blocked (GATE D) -> REAL-REQUIRED
  all others -> MOCK-ACCEPTED

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section..." — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers..." | evaluator-subject form |
  | "Coverage demonstrates that..." | evaluator-subject form |
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

## V-05 — Combined: All Three (Bidirectional ROLE HANDOFF + Three-Bucket GATE B + Phase-Attributed GATE D)

**axis:** combined (V-01 bidirectional ROLE HANDOFF + V-02 GATE B three-bucket partition +
V-03 GATE D phase-attributed INERTIA LEDGER)
**hypothesis:** V-01 makes the ROLE HANDOFF bidirectional — both entering and closed sets
declared at the phase boundary with a SCOREBOARD snapshot. V-02 makes GATE B a complete
three-bucket partition — all 9 namespaces named under auto-flagged, Architect-phase, or
Strategy-phase. V-03 makes the GATE D INERTIA LEDGER phase-attributed — Architect and
Strategy earners separately listed before STEP 5 runs. Together: every major partition
event in the skill (GATE B initial split, GATE C phase boundary, GATE D phase exit) is
independently enumerable without cross-referencing adjacent steps. Each gate becomes a
self-contained partition record. Predicted score against v11: 31/31.

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

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]..."
  FAIL forms: "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..."

Exempt from this rule: tier sourcing output (Tier: N (source: ...)); auto-flag Rule A/B/C
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
  CONSTRAINT: Total flags count. Verify sum before writing partition.
  HALT. If total is inconsistent with Rule A/B/C counts, recount before advancing.

  Partition:

  Auto-flagged bucket: ___
  CONSTRAINT: Name each auto-flagged namespace explicitly as a list under this bucket.
    Count must equal total flags above. Write "Auto-flagged: none" if count is 0.
  HALT. If auto-flagged list is absent or count mismatches total flags, write it before advancing.

  Evaluation universe bucket (Architect-phase + Strategy-phase): ___
  CONSTRAINT: Name each non-flagged namespace explicitly as a list under this bucket.
    Count must equal 9 - total flags. This list is the canonical scope for STEP 3 and STEP 4.
    An anonymous count alone does not satisfy.
  HALT. If evaluation universe list is absent or incomplete, write it before advancing.

  Partition check: ___ auto-flagged + ___ evaluation universe = ___
  CONSTRAINT: Sum must equal 9. All three bucket fields required before advancing.
  HALT. If sum does not equal 9, recount before advancing.

  Do not proceed to STEP 3 until GATE B is written with both named bucket lists.

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Arch-blocked: [namespace] added."
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

  Do not proceed to ROLE HANDOFF until GATE C is written.

---

ROLE HANDOFF — Architect Phase Closed / Strategy Phase Opens

  DECISION SCOREBOARD at handoff:
  REAL-REQUIRED: ___ / MOCK-ACCEPTED: ___
  CONSTRAINT: Copy values from GATE C DECISION SCOREBOARD UPDATE verbatim.
  HALT. If values are absent or do not match GATE C UPDATE exactly, rewrite before advancing.

  INERTIA LEDGER at handoff:
  Arch-blocked (closed as REAL-REQUIRED): ___
  CONSTRAINT: Name each Arch-blocked namespace explicitly. List must match GATE C
    INERTIA LEDGER "Namespaces still at REAL-REQUIRED default" exactly.
  HALT. If Arch-blocked list is absent or any name mismatches GATE C, rewrite before advancing.

  Strategy evaluation universe (entering STEP 4): ___
  CONSTRAINT: Name each namespace from GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" list
    explicitly. These are the only namespaces that enter STEP 4.
  HALT. If this list is absent or any name mismatches GATE C, write it before advancing.

  Partition check: ___ Arch-blocked + ___ entering STEP 4 = ___
  CONSTRAINT: Sum must equal GATE B evaluation universe count. Both sets together account for
    the complete evaluation universe — no namespace is unassigned at this boundary.
  HALT. If sum does not equal GATE B evaluation universe count, reconcile before advancing.

  Do not begin STEP 4 until ROLE HANDOFF is written with all four fields.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Namespaces declared in ROLE HANDOFF only.
DECISION SCOREBOARD applies: each namespace begins REAL-REQUIRED. The Strategy role must
name a positive domain realism argument to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each namespace in the ROLE HANDOFF Strategy evaluation universe, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  HALT. Delete Required artifact citation if it does not begin with the exact form above. Rewrite.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  HALT. Delete SQ if it does not begin with the required form. Rewrite.
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]..."
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

VERDICT-ECHO: Each REAL-REQUIRED -> "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = ROLE HANDOFF entering count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.

  INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default (Strategy-blocked): ___
  Namespaces that have earned MOCK-ACCEPTED against inertia — by phase:

    Architect-phase earners: ___
    CONSTRAINT: Names must match GATE C INERTIA LEDGER "earned MOCK-ACCEPTED" list exactly.
      Count must equal GATE C MOCK-ACCEPTED count.
    HALT. If list is absent or any name mismatches GATE C INERTIA LEDGER, rewrite before advancing.

    Strategy-phase earners: ___
    CONSTRAINT: Names must match this gate's MOCK-ACCEPTED count above. Write "Strategy-phase
      earners: none" if count is 0.
    HALT. If list is absent or count mismatches this gate's MOCK-ACCEPTED, rewrite before advancing.

  Total MOCK-ACCEPTED: ___
  CONSTRAINT: Architect-phase earner count + Strategy-phase earner count = Total MOCK-ACCEPTED.
    Total MOCK-ACCEPTED + Strategy-blocked count = ROLE HANDOFF entering count.
  HALT. If either constraint fails, reconcile before advancing.

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
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for..."
HALT. If any cell does not begin "Without real data for...", replace it with the verbatim
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
  Architect rows: ___. Expected: ___ (= GATE D INERTIA LEDGER Architect-phase earner count).
  Strategy rows: ___. Expected: ___ (= GATE D INERTIA LEDGER Strategy-phase earner count).
  CONSTRAINT: All three counts must match. Per-phase split must equal the corresponding
    INERTIA LEDGER phase-earner tally at GATE D.
  HALT. If any count mismatches, identify the discrepancy against the GATE D phase-earner
    lists and correct the register before proceeding.
  Do not proceed to STEP 6 until GATE E-COST is written with all three counts confirmed.

---

STEP 6 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) -> REAL-REQUIRED
  Arch-blocked (GATE C) -> REAL-REQUIRED
  Strategy-blocked (GATE D) -> REAL-REQUIRED
  all others -> MOCK-ACCEPTED

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
  CONSTRAINT: Begin "The mock artifact's [namespace] section..." — artifact-as-subject required.
  HALT. Delete the Basis field if it does not begin with the required form. Rewrite.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers..." | evaluator-subject form |
  | "Coverage demonstrates that..." | evaluator-subject form |
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
