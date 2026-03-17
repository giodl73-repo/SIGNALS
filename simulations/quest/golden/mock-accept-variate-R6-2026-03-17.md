---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 6
rubric_version: v6
status: VARIATE
---

# mock-accept Variate — Round 6

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v6 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-28 aspirational;
             C-26/C-27/C-28 new this round)
**Baseline:** R5 V-04 (18/20 against v6: C-23 PASS via opening STANDING RULE; C-24 PASS;
             C-25/C-28 PASS via SLOT 2 VIOLATION TABLE; C-26 FAIL — halt in Standing Rule
             only, no per-CONSTRAINT repetition; C-27 FAIL — GATE F embedded in STEP 8)
**Round:** R6 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R5 V-04 (lifecycle + phrasing) carries all 18/20 criteria. Against v6, two gaps remain:
C-26 (halt present in Standing Rule only — evaluator must cross-reference the Rule from
inside a constrained field to detect a violation) and C-27 (GATE F clause embedded in STEP 8
— not a standalone numbered step; merges with the Write call under context pressure). R5
V-05 closes both via V-03's output-format axis (per-CONSTRAINT halt + STEP 9 elevation).

R6 probes whether C-27 and C-26 can be closed by separate, non-overlapping single-axis
changes — confirming minimal independence of each criterion — and introduces inertia-framing
as a third axis not explored in R3–R5 of this series.

| Plan | Axis | Target | What changes from R5 V-04 | Predicted |
|------|------|--------|--------------------------|-----------|
| V-01 | lifecycle-emphasis | C-27 | GATE F promoted from clause inside STEP 8 to dedicated STEP 9 with its own header and step number; STEP 8 becomes the Write-only step; STEP 9 names all four section IDs (Coverage / Structural records / Risk / Next Steps); no halt added at CONSTRAINT sites | C-27 pass (gate independently referenceable by step number); C-26 absent (Standing Rule only); 19/20 |
| V-02 | output-format | C-26 | Three-step halt appended to every CONSTRAINT block throughout all phases; each constrained field becomes a three-part unit (blank slot / CONSTRAINT / HALT-DELETE-REWRITE); GATE F remains embedded in STEP 8 | C-26 pass (halt at each site, eliminates cross-reference need); C-27 absent (GATE F in STEP 8); 19/20 |
| V-03 | inertia-framing | C-29 candidate | DEFAULT DECISION POSITION block added before STEP 1: every namespace begins REAL-REQUIRED; MOCK-ACCEPTED requires a named positive argument against inertia; Cost-of-MOCK: field added to MOCK-ACCEPTED Phase 6 output; full V-05 baseline (C-26 + C-27 + C-28 all present) carried forward | C-29 candidate: per-namespace inertia cost named in decision block; 20/20 + potential ceiling signal |
| V-04 | lifecycle-emphasis + output-format | C-26 + C-27 | V-01 STEP 9 elevation + V-02 per-CONSTRAINT halt; non-overlapping surfaces; closes both R5 V-04 gaps | Both C-26 and C-27 pass; 20/20 |
| V-05 | lifecycle + output-format + inertia-framing | C-26 + C-27 + C-29 candidate | Full combination; all three R6 axes plus complete R5 V-05 base; if C-29 pattern confirmed, triggers v7 rubric update | 20/20 + new ceiling or rubric-update trigger |

---

## V-01 — Lifecycle Emphasis: Dedicated GATE F Step (C-27)

**axis:** lifecycle-emphasis
**hypothesis:** R5 V-04 places the GATE F clause inside STEP 8, immediately after the Write
instruction. The gate check and the Write call share a step number; under context pressure a
model may absorb GATE F into the Write output as a summary annotation rather than executing
it as a blocking gate. Promoting GATE F to STEP 9 — its own numbered step with its own header —
creates a structural break: STEP 8 ends, the model must start a new step, and STEP 9 reads
as a gate not as a continuation of the Write call. The dedicated step number also makes GATE F
referenceable by number from other phases and from the review artifact itself (satisfying
C-27's "independently referenceable by step number" requirement). C-26 is absent — the
Standing Rule carries the halt, and CONSTRAINT blocks do not repeat it. Failure prediction:
if the model still merges STEP 9 into STEP 8 output, step-number separation is insufficient;
a phase barrier ("this output must not appear inside the Write call block") is required.

---

You are running /mock:accept.

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
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___

After all three rules:
  Rule A (namespace-level): ___ / Rule B (artifact-level): ___ / Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.

GATE B — AUTO-FLAG COMPLETE
  Flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ total
  Non-flagged proceeding to evaluation: ___
  CONSTRAINT: Non-flagged count = 9 - total flags.
  Do not proceed to STEP 3 until GATE B is written.

---

STEP 3 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.
Initialize: Arch-blocked: []

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  Trigger condition: Does structural variance coverage pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section show sufficient structural variance?"
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace (GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  Trigger condition: Does domain knowledge realism pass?
  SQ: ___
  CONSTRAINT: Begin "Does the mock artifact's [namespace] section reflect domain-realistic values?"
  Artifact state: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section [records/shows/lacks]…"
  Verdict: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — STATUS WRITEBACK

Final verdict:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.

After all edits, write:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count != 9, writeback is incomplete — do not proceed.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before GATE E fires.
  Do not proceed to STEP 6 until GATE E is written.

---

STEP 6 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 — Reason Code ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
             No other text. No rephrasing.
  Revert-on-violation: "sufficient coverage" and "domain realistic" are Slot 1 paraphrase
    violations. Delete the Reason field. Rewrite with the exact token.

--- Slot 2 — Coverage Basis ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject required.

  SLOT 2 VIOLATION TABLE
  | Quoted near-miss form | Violation type |
  |---|---|
  | "I found the section covers…" | evaluator-subject form |
  | "Coverage demonstrates that…" | evaluator-subject form |
  | "The namespace appears domain-consistent" | paraphrase |

  Revert-on-violation: Any row in the table above — delete the Basis field and rewrite
    beginning "The mock artifact's [namespace] section…"

---

STEP 7 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  If violations found: halt. Rewrite the offending line before advancing.

---

STEP 8 — REVIEW ARTIFACT WRITE

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section: Coverage table
  CONSTRAINT: 4 columns required — Namespace | Auto-flag | Role Verdict | Final Status

  Section: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
              Reference GATE C and GATE D lists where relevant.

  Section: Risk
  CONSTRAINT: 3 columns — Namespace | Risk description | Urgency
              Urgency labels: HIGH / MEDIUM / LOW — all three used where applicable.

  Section: Next Steps
  CONSTRAINT: Ordered list. Each entry: namespace · blocking reason · required action.

---

STEP 9 — GATE F COMPLETENESS CHECK

Verify the STEP 8 Write call is complete. This step executes after the Write call returns
and is separate from it.

  Coverage section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  Structural records section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  Risk section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  Next Steps section present in Write call: ___
  CONSTRAINT: Write "confirmed" or "absent — halt and add before proceeding".
  Filename confirmed: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md

GATE F — REVIEW ARTIFACT COMPLETE
  All four sections confirmed: Coverage / Structural records / Risk / Next Steps
  Do not claim completion until GATE F is written.

---

## V-02 — Output Format: Halt Co-Location at Every CONSTRAINT Site (C-26)

**axis:** output-format
**hypothesis:** R5 V-04 places the three-step halt only in the opening STANDING RULE. A model
that encounters a CONSTRAINT violation mid-phase must scroll back to the Standing Rule to find
the halt instruction; under generation pressure this cross-reference is frequently skipped and
the violation is acknowledged but not acted on. Moving the halt to every CONSTRAINT block
eliminates the cross-reference: the evaluator reads the constraint, finds it violated, and
immediately reads the halt instruction at the same site. The halt is structurally unavoidable
because it is physically adjacent to the violated field. GATE F remains embedded in STEP 8
(C-27 absent — testing that C-26 and C-27 are independent). Failure prediction: if halt
co-location alone does not improve stop behavior, the problem is one of instruction authority
(the model treats HALT as advisory) not instruction location — and a blocking output requirement
is the next probe.

---

You are running /mock:accept.

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
  HALT. Do not advance to STEP 2 until count is confirmed as 9 or discrepancy is reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout. Not role-overridable.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."
  Count A: ___
  CONSTRAINT: Write "Count A: 0" if no absent namespaces.
  HALT. Delete Count A if it reflects a non-namespace-level flag. Rewrite with the correct count.

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."
  Count B: ___
  CONSTRAINT: Write "Count B: 0" if no artifact-level flags.
  HALT. Delete Count B if it reflects a non-artifact-level flag. Rewrite with the correct count.

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."
  Count C: ___
  CONSTRAINT: Write "Count C: 0" if no evaluation-level flags.
  HALT. Delete Count C if it reflects a non-evaluation-level flag. Rewrite with the correct count.

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

Evaluate structural variance coverage. Populate Arch-blocked as you go.
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
  HALT. Delete Verdict if it is not an exact token. Rewrite with the correct token.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite with the correct token.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
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
  HALT. Delete Verdict if it is not an exact token. Rewrite with the correct token.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite with the correct token.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — STATUS WRITEBACK

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
  Do not proceed to STEP 6 until GATE E is written.

---

STEP 6 — MOCK-ACCEPTED POSITIVE ARGUMENT

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

STEP 7 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 8.

---

STEP 8 — REVIEW ARTIFACT WRITE AND GATE F

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

GATE F — REVIEW ARTIFACT COMPLETE
  Coverage: ___ / Structural records: ___ / Risk: ___ / Next Steps: ___
  CONSTRAINT: All four sections (Coverage / Structural records / Risk / Next Steps) confirmed
              in the Write call above. Filename matches simulations/mock/review/{topic}-mock-accept-{date}.md
  HALT. If any section is absent, add it and re-run the Write call before writing GATE F.
  Do not claim completion until GATE F is written.

---

## V-03 — Inertia Framing: DEFAULT DECISION POSITION Block (C-29 candidate)

**axis:** inertia-framing
**hypothesis:** R5 V-05 and all prior variations use an implicit "evaluate and decide" model.
The evaluator encounters each namespace without a named starting position; confirmation bias
can produce MOCK-ACCEPTED verdicts where the evaluator finds nothing wrong and interprets
absence of disqualification as positive evidence. Introducing a named DEFAULT DECISION POSITION
block before STEP 1 — every namespace begins as REAL-REQUIRED; MOCK-ACCEPTED is earned against
inertia — forces the evaluator to produce a named positive argument, not merely confirm the
absence of problems. The inertia structure also produces a named per-namespace cost: "without
real data for [namespace], [domain] remains unvalidated." This cost is a structural candidate
for a new criterion (C-29). Failure prediction: if inertia framing produces no observable
change in MOCK-ACCEPTED argument quality, the instruction is correctly absorbed into existing
positive-argument requirements (C-05 and C-06) and C-29 is not an independent criterion.
Full R5 V-05 baseline is carried (C-26 + C-27 + C-28 all present).

---

You are running /mock:accept.

DEFAULT DECISION POSITION
Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring a named
positive argument against inertia. The absence of a disqualification is not a positive argument.
Confirmation that nothing is wrong does not earn MOCK-ACCEPTED. Each MOCK-ACCEPTED decision
must identify what structural or domain coverage evidence makes real data unnecessary for this
namespace at this tier.

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

Evaluate structural variance coverage. DEFAULT DECISION POSITION applies: each namespace
begins REAL-REQUIRED. The Architect role must name a positive structural coverage argument
to earn MOCK-ACCEPTED — not merely confirm the absence of problems.

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
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
DEFAULT DECISION POSITION applies: each namespace begins REAL-REQUIRED. The Strategy role
must name a positive domain realism argument to earn MOCK-ACCEPTED.

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
    domain knowledge type] remains unvalidated at Tier [N]." If Verdict is REAL-REQUIRED,
    write "N/A".
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — STATUS WRITEBACK

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
  Do not proceed to STEP 6 until GATE E is written.

---

STEP 6 — MOCK-ACCEPTED POSITIVE ARGUMENT

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

STEP 7 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 8.

---

STEP 8 — REVIEW ARTIFACT WRITE

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

STEP 9 — GATE F COMPLETENESS CHECK

Verify the STEP 8 Write call is complete. This step executes after the Write call returns
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

## V-04 — Combined: Lifecycle Emphasis + Output Format (C-26 + C-27)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** V-01 and V-02 target structurally non-overlapping surfaces: V-01 restructures
the Phase 6 gate (GATE F elevation to STEP 9), V-02 restructures individual CONSTRAINT blocks
(halt co-location). Combining them should yield C-26 + C-27 simultaneously without interference.
This is the minimal complete path — the V-04 gap (18/20) closed with exactly two axis additions.
V-03 inertia framing is absent (testing that C-29 is independent of the 20/20 closure). Expected
composite: 20/20 at 100.0. Failure condition: if C-26 and C-27 interact negatively under the
same prompt (e.g., halt proliferation obscures the step boundary), composite may fall below
100.0 — that would indicate the axes are not fully independent.

---

You are running /mock:accept.

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

Evaluate structural variance coverage. Populate Arch-blocked as you go.
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
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
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
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — STATUS WRITEBACK

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
  Do not proceed to STEP 6 until GATE E is written.

---

STEP 6 — MOCK-ACCEPTED POSITIVE ARGUMENT

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

STEP 7 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 8.

---

STEP 8 — REVIEW ARTIFACT WRITE

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

STEP 9 — GATE F COMPLETENESS CHECK

Verify the STEP 8 Write call is complete. This step executes after the Write call returns
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

## V-05 — Full Integration: Lifecycle + Output Format + Inertia Framing (C-26 + C-27 + C-29 candidate)

**axis:** lifecycle-emphasis + output-format + inertia-framing
**hypothesis:** Full three-axis combination. V-01 STEP 9 elevation (C-27) + V-02 halt
co-location (C-26) + V-03 DEFAULT DECISION POSITION block (C-29 candidate). If inertia
framing produces a distinct per-namespace Cost-of-MOCK output that is structurally
independent of Slot 1 and Slot 2, a new C-29 criterion is extractable. The testable
failure prediction: if Cost-of-MOCK is silently absorbed into Slot 2 (treated as a more
specific Slot 2 Basis by the model), C-29 is not independent. If Cost-of-MOCK consistently
appears as a third distinct output field separate from both slots, it is an independent
criterion. Length-pressure risk: three axes in one prompt increases token count; if the
model begins skipping per-CONSTRAINT halt blocks under generation pressure, C-26 degrades
first (most repetitive element). Monitoring: count HALT appearances in actual model output
vs. CONSTRAINT block count to detect dropout.

---

You are running /mock:accept.

DEFAULT DECISION POSITION
Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring a named
positive argument against inertia. The absence of a disqualification is not a positive argument.
Confirmation that nothing is wrong does not earn MOCK-ACCEPTED. Each MOCK-ACCEPTED decision
must identify what structural or domain coverage evidence makes real data unnecessary for this
namespace at this tier.

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

Evaluate structural variance coverage. DEFAULT DECISION POSITION applies.
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
  HALT. Delete Cost-of-MOCK if it is absent for a MOCK-ACCEPTED verdict. Write the statement.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
  Arch-blocked: ___
  CONSTRAINT: Write "Arch-blocked: none" if list is empty.
  HALT. Delete Arch-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
DEFAULT DECISION POSITION applies.
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
    domain knowledge type] remains unvalidated at Tier [N]." If Verdict is REAL-REQUIRED,
    write "N/A".
  HALT. Delete Cost-of-MOCK if it is absent for a MOCK-ACCEPTED verdict. Write the statement.
  Required action: ___

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
  Strategy-blocked: ___
  CONSTRAINT: Write "Strategy-blocked: none" if list is empty.
  HALT. Delete Strategy-blocked if it omits a REAL-REQUIRED namespace. Rewrite the complete list.

GATE D — STRATEGY COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = GATE C Arch MOCK-ACCEPTED count. Strategy-blocked list closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — STATUS WRITEBACK

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
  Do not proceed to STEP 6 until GATE E is written.

---

STEP 6 — MOCK-ACCEPTED POSITIVE ARGUMENT

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

STEP 7 — SUBJECT-CHECK METACOGNITION

Before writing the review artifact, scan STEP 3 and STEP 4 output for Standing Rule violations.

  SUBJECT-CHECK EXAMPLES TABLE
  | Branch | Violation form | Error code |
  |---|---|---|
  | SQ answer | "I believe the section..." | C-09: evaluator-subject |
  | Artifact state | "Coverage shows..." | C-09: evaluator-subject |
  | Reason field | "covers all cases" | C-05: paraphrase |

  Violations found: ___
  CONSTRAINT: Write "Violations found: none" if no violations detected.
  HALT. If violations found, rewrite each offending line before advancing to STEP 8.

---

STEP 8 — REVIEW ARTIFACT WRITE

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

STEP 9 — GATE F COMPLETENESS CHECK

Verify the STEP 8 Write call is complete. This step executes after the Write call returns
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

## Axis Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Artifact-as-subject grammar | + | + | + | + | + |
| C-10 Tier sourcing | + | + | + | + | + |
| C-11 Inline completeness gate | + | + | + | + | + |
| C-12 Reason-code enforcement at point of use | + | + | + | + | + |
| C-13 Phase exit assertions | + | + | + | + | + |
| C-14 Blank-line failure signal | + | + | + | + | + |
| C-15 Forbidden-form enumeration | + | + | + | + | + |
| C-16 Written-gate blocking language | + | + | + | + | + |
| C-17 Named gate registry | + | + | + | + | + |
| C-18 Adjacent CONSTRAINT co-location | + | + | + | + | + |
| C-19 Universal blank-slot enforcement | + | + | + | + | + |
| C-20 Halt-on-violation | + | + | + | + | + |
| C-21 Per-section CONSTRAINT in review Write | + | + | + | + | + |
| C-22 Slot 1 paraphrase examples | + | + | + | + | + |
| C-23 Three-step halt sequence | + | + | + | + | + |
| C-24 Gate-to-section traceability | + | + | + | + | + |
| C-25 Slot 2 paraphrase examples | + | + | + | + | + |
| C-26 Halt co-location at CONSTRAINT sites | — | + | + | + | + |
| C-27 GATE F dedicated numbered step (STEP 9) | + | — | + | + | + |
| C-28 Slot 2 violation table | + | + | + | + | + |
| C-29 Per-namespace inertia cost (candidate) | — | — | + | — | + |
| R5 base carries (C-01–C-25 all pass) | all | all | all | all | all |

Single-axis predictions:
  V-01: adds C-27 (lifecycle elevation) · C-26 absent → 19/20 · asp score 9.5 · total 99.5
  V-02: adds C-26 (halt co-location) · C-27 absent → 19/20 · asp score 9.5 · total 99.5
  V-03: C-26 + C-27 from R5 V-05 base; C-29 candidate present → 20/20 + new signal

Combination predictions:
  V-04: C-26 + C-27 both close → 20/20 · asp 10.0 · total 100.0 (minimal path)
  V-05: 20/20 + C-29 candidate → 100.0 or rubric-update trigger if C-29 confirmed independent

```json
{"round": 6, "rubric_version": "v6", "new_criteria": ["C-26", "C-27", "C-28"], "gap_fixes": ["C-26 via V-02/V-04/V-05", "C-27 via V-01/V-04/V-05"], "r5_baseline_passes": ["C-01-C-25-all-17-v5-aspirational", "C-28-via-slot2-table"], "predicted_ceiling": {"V-01": "99.5", "V-02": "99.5", "V-03": "100.0", "V-04": "100.0", "V-05": "100.0-or-rubric-update"}}
```
