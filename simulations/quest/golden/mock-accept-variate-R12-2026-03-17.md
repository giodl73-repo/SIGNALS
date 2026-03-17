---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 12
rubric_version: v12
status: VARIATE
---

# mock-accept Variate — Round 12

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v12 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-43 aspirational;
             C-40/C-41/C-42/C-43 new this round; denominator 35)
**Baseline:** R11 V-05 (sole golden, 35/35 against v12: bidirectional ROLE HANDOFF +
             named GATE C destination + phase-attributed GATE D INERTIA LEDGER +
             GATE E-COST cross-reference to GATE D sub-lists + three-bucket GATE B)
**Round:** R12 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R11 V-05 is the sole golden at 35/35 against v12. The four R12 criteria
(C-40/C-41/C-42/C-43) tightened verifiability at the Architect-to-Strategy boundary
(bidirectional ROLE HANDOFF), the Strategy phase exit (phase-attributed GATE D
INERTIA LEDGER), the COST REGISTER cross-check source (GATE D sub-lists), and the
GATE C exit traceability link (named ROLE HANDOFF destination). R12 probes three
structural questions that R11 V-05 leaves open:

1. C-43 creates an explicit gate-to-construct link at GATE C by naming "ROLE HANDOFF"
   rather than "STEP 4". GATE D exits to "STEP 5" (step number) and GATE E-COST exits
   to "STEP 6" (step number). The principle underlying C-43 — name the destination by
   construct identity, not step number — is satisfied at one gate boundary but not the
   others. Does extending named-destination exits to GATE D (→ GATE E-COST) and
   GATE E-COST (→ STATUS WRITEBACK) create a fully-linked gate-exit chain throughout
   the skill, making every gate-to-gate transition traceable by construct name without
   consulting the step numbering scheme?

2. GATE E-COST (C-42) verifies the COST REGISTER's phase-row counts against GATE D's
   phase-earner sub-lists before the STEP 9 Write call. GATE F verifies that the Write
   call's sections are present and structurally complete, but GATE F does not re-verify
   the COST REGISTER's phase-row counts against GATE D. If GATE F adds explicit
   phase-row count assertions (Architect rows in artifact vs GATE D Architect-phase
   earners; Strategy rows vs GATE D Strategy-phase earners), the post-write verification
   layer matches the pre-write verification at GATE E-COST — the artifact's COST
   REGISTER phase attribution is independently auditable at GATE F without re-reading
   GATE E-COST or STEP 5.

3. The DECISION SCOREBOARD records the opening state (9/0) and receives its first
   explicit gate-level update at ROLE HANDOFF (copied from GATE C). Between GATE A and
   ROLE HANDOFF, the score is implicit — no movement has occurred, but no checkpoint
   states this explicitly. GATE B resolves the auto-flagged set (permanently
   REAL-REQUIRED) and opens the evaluation universe, but does not carry a SCOREBOARD
   STATE. Does adding SCOREBOARD STATE at GATE A (9/0 confirmed — evaluation not yet
   begun) and GATE B (auto-flagged resolved; evaluation universe pending —
   MOCK-ACCEPTED still 0) make the zero-movement pre-evaluation phase explicitly
   verifiable, preventing accidental score attribution before STEP 3 runs?

| Plan | Axis | Target | What changes from R11 V-05 | Predicted |
|------|------|--------|---------------------------|-----------|
| V-01 | lifecycle-emphasis (named gate destination chain) | GATE D + GATE E-COST exits | GATE D: "Do not proceed to GATE E-COST"; GATE E-COST: "Do not proceed to STATUS WRITEBACK" | 35/35 |
| V-02 | output-format (GATE F phase-row cross-verification) | GATE F | GATE F adds COST REGISTER Architect-rows vs GATE D Architect-earners + Strategy-rows vs GATE D Strategy-earners; summary line updated | 35/35 |
| V-03 | inertia-framing (SCOREBOARD at GATE A and GATE B) | GATE A + GATE B | GATE A adds SCOREBOARD STATE 9/0; GATE B adds SCOREBOARD STATE auto-flagged resolved / MOCK-ACCEPTED still 0 | 35/35 |
| V-04 | combined: lifecycle + output-format | V-01 + V-02 | Named gate destination chain + GATE F phase-row cross-verification | 35/35 |
| V-05 | combined: all three | V-01 + V-02 + V-03 | Named destinations + GATE F cross-verification + SCOREBOARD at GATE A/B | 35/35 |

---

## V-01 — Lifecycle Emphasis: Named Gate Destination Chain

**axis:** lifecycle-emphasis (named gate destination chain)
**hypothesis:** C-43 requires GATE C to name "ROLE HANDOFF" as its blocking destination
rather than "STEP 4". GATE D exits with "Do not proceed to STEP 5 until GATE D is
written" and GATE E-COST exits with "Do not proceed to STEP 6 until GATE E-COST is
written" — both use step numbers. The principle underlying C-43 is that naming the
destination by construct identity (ROLE HANDOFF) rather than step number (STEP 4)
creates an explicit gate-to-construct link that is traceable without knowing the
step numbering scheme. V-01 extends this principle: GATE D exits to "GATE E-COST"
(the named gate, not "STEP 5") and GATE E-COST exits to "STATUS WRITEBACK" (the
named step function, not "STEP 6"). The full gate-exit chain is then: GATE C →
ROLE HANDOFF → (no gate) → GATE D → GATE E-COST → STATUS WRITEBACK. Each exit
names its destination by construct identity. All other steps identical to R11 V-05.
Predicted score against v12: 35/35.

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
  CONSTRAINT: Sum must equal 9. Both bucket fields required before advancing.
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

  Do not proceed to GATE E-COST until GATE D is written.
  [V-01 CHANGE: "GATE E-COST" replaces "STEP 5"]

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
  Do not proceed to STATUS WRITEBACK until GATE E-COST is written with all three counts confirmed.
  [V-01 CHANGE: "STATUS WRITEBACK" replaces "STEP 6"]

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

## V-02 — Output Format: GATE F Phase-Row Cross-Verification

**axis:** output-format (GATE F phase-row cross-verification against GATE D sub-lists)
**hypothesis:** GATE E-COST (C-42) verifies the COST REGISTER's phase-row counts against
GATE D's phase-earner sub-lists before the STEP 9 Write call. GATE F verifies that the
written artifact's sections are present and structurally complete, but does not re-verify
the COST REGISTER's phase-row counts against GATE D after the Write call returns. The
pre-write verification (GATE E-COST) and the post-write verification (GATE F) currently
cover different dimensions: GATE E-COST covers count accuracy, GATE F covers section
presence. If GATE F adds explicit phase-row count assertions — COST REGISTER Architect
rows in the written artifact vs GATE D Architect-phase earners count; Strategy rows vs
GATE D Strategy-phase earners count — the artifact's COST REGISTER phase attribution is
independently verifiable at GATE F without re-reading GATE E-COST or STEP 5. The two
verification layers become symmetric: pre-write count verification at GATE E-COST, post-
write count verification at GATE F. All other steps identical to R11 V-05. Predicted
score against v12: 35/35.

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
  CONSTRAINT: Sum must equal 9. Both bucket fields required before advancing.
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

  COST REGISTER phase-row cross-verification:
  [V-02 CHANGE: two new assertions added to GATE F]
  COST REGISTER Architect rows in artifact: ___. Expected: ___ (= GATE D Architect-phase earners count).
  CONSTRAINT: Write "confirmed" or "Architect row count mismatches GATE D — halt and correct
    the COST REGISTER in the artifact and re-run the Write call before proceeding".
  HALT. If mismatch, re-open the Write call, correct the COST REGISTER Architect rows, and
    re-run before advancing.
  COST REGISTER Strategy rows in artifact: ___. Expected: ___ (= GATE D Strategy-phase earners count).
  CONSTRAINT: Write "confirmed" or "Strategy row count mismatches GATE D — halt and correct
    the COST REGISTER in the artifact and re-run the Write call before proceeding".
  HALT. If mismatch, re-open the Write call, correct the COST REGISTER Strategy rows, and
    re-run before advancing.

GATE F — REVIEW ARTIFACT COMPLETE
  All sections confirmed with content structure and phase attribution verified:
    Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column /
    Next Steps: ordered list / COST REGISTER: phase-row counts match GATE D sub-lists
  Do not claim completion until GATE F is written.
