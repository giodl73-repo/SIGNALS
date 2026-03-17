---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 8
rubric_version: v8
status: VARIATE
---

# mock-accept Variate — Round 8

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v8 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-32 aspirational;
             C-31/C-32 new this round; denominator 24)
**Baseline:** R7 V-05 (sole golden, 24/24 against v8: C-31 via INERTIA LEDGER at GATE C/GATE D;
             C-32 via dedicated STEP 5 MOCK COST REGISTER with GATE E-COST; all prior criteria retained)
**Round:** R8 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R7 V-05 is the sole golden at 24/24 against v8. R7 V-03 and V-04 are co-silvers at 23/24
(INERTIA LEDGER present, MOCK COST REGISTER absent). R8 probes three structural questions:

1. Does C-32's "independently verifiable audit surface" depend on format (table vs. field-list),
   or only on placement (dedicated step + own gate before writeback)?

2. Does C-32 strictly require a distinct numbered step, or does a named sub-block embedded
   within GATE D satisfy "dedicated step with its own gate"?

3. Does C-31 strictly require gate-exit position (inside GATE C/GATE D after all per-namespace
   evaluations), or does a gate-entry declaration (before the evaluation loop begins) satisfy?

| Plan | Axis | Target | What changes from R7 V-05 | Predicted |
|------|------|--------|---------------------------|-----------|
| V-01 | output-format (COST REGISTER table) | C-32 format independence | STEP 5 field-list replaced with 3-column table; GATE E-COST unchanged | 24/24 |
| V-02 | lifecycle-emphasis (COST REGISTER merge) | C-32 dedicated-step test | STEP 5 removed; aggregation embedded as named sub-block within GATE D; GATE E-COST absorbed; STEP 5–9 renumber | C-32 FAIL — 23/24 |
| V-03 | inertia-framing (LEDGER entry vs. exit) | C-31 position test | INERTIA LEDGER blocks moved from gate-exit (inside GATE C/GATE D) to gate-entry (before STEP 3 and STEP 4 loops); gates retain count assertions only | C-31 FAIL — 23/24 |
| V-04 | output-format + lifecycle-emphasis (extended GATE E-COST) | C-32 clarity extension | V-01 table + GATE E-COST extended with explicit column-traceability naming (Namespace, Phase, Cost-of-MOCK) parallel to GATE F section naming | 24/24 |
| V-05 | output-format + inertia-framing + phrasing-register | full integration with formal register | V-01 table + GATE D INERTIA LEDGER extended with cumulative cross-phase sum assertion + formal declarative surrounding prose; HALT/DELETE/REWRITE triples preserved verbatim | 24/24 |

---

## V-01 — Output Format: MOCK COST REGISTER as 3-Column Table

**axis:** output-format (COST REGISTER format)
**hypothesis:** R7 V-05 presents the MOCK COST REGISTER as a per-namespace field-list
(Namespace: ___ / Phase: ___ / Cost-of-MOCK: ___). C-32 requires "a single independently
verifiable pre-writeback audit surface" — but does not specify format. A 3-column table
(Namespace | Phase | Cost-of-MOCK) presents the same information in a more scannable form
that is independently verifiable by inspection without parsing field labels. The count
assertion and GATE E-COST are structurally unchanged. If C-32 is format-independent, V-01
scores 24/24. If C-32 requires the field-list structure specifically, V-01 still satisfies
the "distinct numbered step with own gate" requirement. All other steps identical to R7 V-05.
Predicted score against v8: 24/24.

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

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table:

| Namespace | Phase | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Rows confirmed: ___. Expected: ___.
  Do not proceed to STEP 6 until GATE E-COST is written.

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

## V-02 — Lifecycle Emphasis: COST REGISTER Merged into GATE D

**axis:** lifecycle-emphasis (COST REGISTER placement)
**hypothesis:** R7 V-05 places MOCK COST REGISTER as a dedicated STEP 5 between GATE D and
STATUS WRITEBACK. C-32 requires "a distinct numbered step with its own gate, placed before
writeback." This variation tests the minimum structural interpretation: the register logic
is moved inside GATE D as a named sub-block (COST REGISTER — STRATEGY PHASE EXIT), appearing
after the INERTIA LEDGER within the gate. GATE E-COST becomes a sub-gate within GATE D rather
than a standalone gate. If C-32 strictly requires an independently numbered step, this fails.
If C-32's "distinct" requirement is satisfied by a named block with its own gate assertion
(regardless of step numbering), this passes. Predicted: C-32 FAIL — rubric specifies "distinct
numbered step"; step number is the structural separator. 23/24 (99.58).
STEP numbering: original STEP 5–9 become STEP 5–9 with writeback at STEP 5.

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

  COST REGISTER — STRATEGY PHASE EXIT
  List all MOCK-ACCEPTED namespaces from GATE C and GATE D combined:
    Namespace: ___ | Phase: ___ | Cost-of-MOCK: ___
    [repeat for each MOCK-ACCEPTED namespace]
  CONSTRAINT: Each Cost-of-MOCK entry must be copied verbatim from the evaluation record
    above. Each entry must begin "Without real data for…"
  HALT. If any entry does not begin "Without real data for…", rewrite from source record.
  COST REGISTER ASSERTION: Entries recorded: ___. Expected: ___ (= total MOCK-ACCEPTED).
  CONSTRAINT: Count must equal total MOCK-ACCEPTED namespaces.
  HALT. If count is wrong, identify missing entries and add them.

  GATE E-COST — COST REGISTER COMPLETE
    Entries confirmed: ___. Expected: ___.

  Do not proceed to STEP 5 until GATE D and GATE E-COST are written.

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

## V-03 — Inertia Framing: LEDGER at Gate Entry, Not Gate Exit

**axis:** inertia-framing (LEDGER position)
**hypothesis:** R7 V-05 places the INERTIA LEDGER inside GATE C (after all Architect
evaluations) and inside GATE D (after all Strategy evaluations) — gate-exit position.
C-31 says "fires at phase exit — not at spec preamble and not within the per-namespace
evaluation record." This variation tests whether "phase exit" is satisfied by gate-entry
position: the INERTIA LEDGER is placed immediately before the STEP 3 evaluation loop
(declaring the initial inertia state before any namespace is evaluated) and immediately
before the STEP 4 evaluation loop. The gates retain count assertions only. If C-31 strictly
requires the LEDGER to be inside the gate at phase exit, this fails. If "phase exit" is
interpreted more loosely as "boundary between phases", the pre-loop placement may satisfy.
All other criteria carried from R7 V-05 (STEP 5 MOCK COST REGISTER present).
Predicted score against v8: C-31 FAIL — 23/24 (99.58).

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

INERTIA LEDGER — ARCHITECT PHASE ENTRY
Declare inertia state before Architect evaluation begins.
  Namespaces pending Architect evaluation: ___ (= non-auto-flagged count from GATE B)
  MOCK-ACCEPTED earned so far: 0
  REAL-REQUIRED remaining: ___ (= non-auto-flagged count)
  CONSTRAINT: Pending count must equal non-auto-flagged count from GATE B.
  HALT. If count does not match, recount before beginning STEP 3.

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
  Do not proceed to STEP 4 until GATE C is written.

---

INERTIA LEDGER — STRATEGY PHASE ENTRY
Declare inertia state before Strategy evaluation begins.
  Namespaces passing to Strategy evaluation: ___ (= GATE C MOCK-ACCEPTED count)
  MOCK-ACCEPTED earned in Architect phase: ___
  REAL-REQUIRED from Architect phase: ___ (= auto-flagged + Arch-blocked)
  Namespaces pending Strategy evaluation: ___
  CONSTRAINT: Pending count must equal GATE C MOCK-ACCEPTED count.
  HALT. If count does not match, recount before beginning STEP 4.

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
  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

For each MOCK-ACCEPTED namespace (from GATE C and GATE D combined):
  Namespace: ___
  Phase: ___  (Architect | Strategy)
  Cost-of-MOCK: ___
  CONSTRAINT: Copy verbatim from the evaluation record above. Do not paraphrase.
  HALT. If the cost statement does not begin "Without real data for…", rewrite it
    from the source evaluation record.

After all entries:
  COST REGISTER ASSERTION: Cost-of-MOCK entries recorded: ___. Expected: ___ (= total MOCK-ACCEPTED
    across GATE C and GATE D).
  CONSTRAINT: Count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED namespace
    has no Cost-of-MOCK entry, add it before advancing.
  HALT. If count is wrong, identify missing entries and add them.

GATE E-COST — COST REGISTER COMPLETE
  Entries confirmed: ___. Expected: ___.
  Do not proceed to STEP 6 until GATE E-COST is written.

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

## V-04 — Combined: Table COST REGISTER + Extended GATE E-COST Column Traceability

**axis:** output-format (table REGISTER) + lifecycle-emphasis (extended GATE E-COST)
**hypothesis:** V-01's 3-column table satisfies C-32 by format. This variation extends
GATE E-COST to explicitly name the register columns it is asserting over (Namespace, Phase,
Cost-of-MOCK), parallel to GATE F naming its sections (Coverage, Structural records, Risk,
Next Steps). C-24 applies to GATE F: "explicitly names the review artifact sections it covers
by their stable IDs." GATE E-COST is a different gate covering a different structure (the
COST REGISTER table, not the review artifact). If C-24 applies only to GATE F, the extension
is neutral. If the pattern generalizes, GATE E-COST column naming produces a signal. Either
way, column-naming makes GATE E-COST more specific and resistant to drift. INERTIA LEDGER
at GATE C and GATE D unchanged from R7 V-05. All other criteria unchanged.
Predicted score against v8: 24/24.

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

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

Collect all Cost-of-MOCK entries from STEP 3 and STEP 4 into a named registry.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table:

| Namespace | Phase | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= total MOCK-ACCEPTED across
  GATE C and GATE D).
CONSTRAINT: Row count must equal total MOCK-ACCEPTED namespaces. If any MOCK-ACCEPTED
  namespace is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Columns confirmed: Namespace | Phase | Cost-of-MOCK
  Rows confirmed: ___. Expected: ___.
  CONSTRAINT: All three columns must be present. If any column is absent, add it before
    advancing.
  HALT. If any column is absent, add it and re-check the table before advancing.
  Do not proceed to STEP 6 until GATE E-COST is written.

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

## V-05 — Full Integration: Table REGISTER + Cumulative GATE D Ledger + Formal Register

**axis:** output-format + inertia-framing (cumulative cross-phase sum) + phrasing-register
**hypothesis:** Three extensions over R7 V-05:
(1) Table format for MOCK COST REGISTER (V-01 axis — C-32 format probe).
(2) GATE D INERTIA LEDGER extended with a cumulative cross-phase sum assertion: after the
per-phase tally, an additional line declares total MOCK-ACCEPTED earned across both phases.
This extends C-31's gate-exit ledger with a cross-phase view that is not reducible to either
the per-phase GATE C or per-phase GATE D tally alone. Does not conflict with C-31 (which
requires the per-phase tally — this adds to it).
(3) Formal declarative prose register in surrounding instructional text — step headers use
"The [role] evaluates…" and "For each namespace…the following record is required:" form rather
than bare imperative. CONSTRAINT/HALT/DELETE/REWRITE triples are kept verbatim throughout;
only the surrounding prose shifts register. Tests whether C-16, C-20, C-23, C-26 survive
a prose-level register shift when the structural HALT triples are preserved.
Predicted score against v8: 24/24. C-23 and C-26 safe because HALT/DELETE/REWRITE triples
are untouched. C-16 safe because "Do not proceed until" language is preserved at gate exits.

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

These FAIL forms are forbidden. When your output contains a forbidden form:
  HALT. Delete the violating line. Rewrite in PASS form.
The rule is active throughout all steps.

---

STEP 1 — ORIENT

The opening step reads the mock artifact and establishes the tier and namespace inventory.
For the artifact under review, write the following fields:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with source label.
  HALT. Delete the Tier field if source label is absent. Rewrite with the exact format.
  Namespaces present: ___
  Namespaces absent: ___

The 9 namespaces are: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. If count != 9, halt and report discrepancy before advancing.
  HALT. Do not advance to STEP 2 until count confirmed or discrepancy reported.
  Do not proceed to STEP 2 until GATE A is written.

---

STEP 2 — AUTO-FLAG

The auto-flag phase applies three mandatory rules to all 9 namespaces. These rules operate
on the artifact directly and are not overridable by role evaluation.
Artifact-as-subject form is required throughout.

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

After all three rules, the partition summary is required:
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

The Architect role evaluates structural variance coverage for each non-auto-flagged namespace.
The DEFAULT DECISION POSITION governs this phase: each namespace begins REAL-REQUIRED.
A positive structural coverage argument is required to earn MOCK-ACCEPTED — confirming the
absence of problems does not satisfy.

Initialize: Arch-blocked: []

For each non-auto-flagged namespace, the following evaluation record is required:
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

  Do not proceed to STEP 4 until GATE C is written.

---

STEP 4 — STRATEGY EVALUATION

The Strategy role evaluates domain knowledge realism for Architect-ACCEPTED namespaces only.
The DEFAULT DECISION POSITION governs this phase: each namespace begins REAL-REQUIRED.
A positive domain realism argument is required to earn MOCK-ACCEPTED.

Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace (GATE C), the following evaluation record is required:
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
  Cumulative MOCK-ACCEPTED earned across both phases: ___
  CONSTRAINT: Must equal GATE C MOCK-ACCEPTED + GATE D MOCK-ACCEPTED. This is the total count
    of namespaces proceeding to MOCK-ACCEPTED status in writeback.
  HALT. If cumulative count does not match GATE C + GATE D totals, recheck before advancing.

  Do not proceed to STEP 5 until GATE D is written.

---

STEP 5 — MOCK COST REGISTER

The MOCK COST REGISTER collects all Cost-of-MOCK entries from STEP 3 and STEP 4 into a
single independently verifiable registry before writeback begins.
One entry per namespace that received MOCK-ACCEPTED in either evaluation phase.

Write a 3-column table:

| Namespace | Phase | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |

CONSTRAINT: Each Cost-of-MOCK cell must contain the verbatim statement copied from the
  evaluation record above. Do not paraphrase. Each cell must begin "Without real data for…"
HALT. If any cell does not begin "Without real data for…", replace it with the verbatim
  statement from the source evaluation record.

COST REGISTER ASSERTION: Rows in table: ___. Expected: ___ (= cumulative MOCK-ACCEPTED from
  GATE D INERTIA LEDGER).
CONSTRAINT: Row count must equal cumulative MOCK-ACCEPTED. If any MOCK-ACCEPTED namespace
  is missing a row, add it before advancing.
HALT. If count is wrong, identify missing rows and add them.

GATE E-COST — COST REGISTER COMPLETE
  Rows confirmed: ___. Expected: ___.
  Do not proceed to STEP 6 until GATE E-COST is written.

---

STEP 6 — STATUS WRITEBACK

The writeback phase applies final verdicts to all 9 namespaces using the Edit tool.
Final verdict routing:
  auto-flagged (GATE B) → REAL-REQUIRED
  Arch-blocked (GATE C) → REAL-REQUIRED
  Strategy-blocked (GATE D) → REAL-REQUIRED
  all others → MOCK-ACCEPTED

For each namespace, the Edit tool writes:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  HALT. Delete Status if it is not an exact token. Rewrite.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  HALT. Delete Reason if it is not an exact token. Rewrite.

After all edits are complete, the canary check is required:
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

For each namespace with final verdict MOCK-ACCEPTED, both slots are required.
Do not merge the slots. Paraphrase is a violation in both slots.

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
The following table identifies the relevant branches and violation forms:

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

All sections are written in ONE Write call. No sections appear outside this Write block.
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

This step verifies the STEP 9 Write call is complete. It executes after the Write call
returns and is structurally separate from it.

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
