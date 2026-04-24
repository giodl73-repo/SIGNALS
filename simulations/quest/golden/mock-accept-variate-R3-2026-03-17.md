---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-17
round: 3
rubric_version: v3
status: VARIATE
---

# mock-accept Variate — Round 3 (rubric v3 revised)

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v3 revised (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-18 aspirational;
             C-15/C-16/C-17/C-18 new this round; C-10/C-14 identified gaps from R2)
**Baseline:** R2 champion (V-04 at 86.7: passes C-09, C-11, C-12, C-13; misses C-10, C-14)
**Round:** R3 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R2 converged on artifact-as-subject standing rule (C-09), inline count assertions (C-11),
reason-code at point of use (C-12), and phase exit assertions (C-13). All four carry forward.
R3 targets the four new aspirational criteria plus the two identified R2 gaps.

| Plan | Axis | Source criterion | What changes | Predicted |
|------|------|-----------------|--------------|-----------|
| V-01 | lifecycle-emphasis | C-16/C-17: written-gate + named registry | All phase transitions become named GATE A–F assertions; each includes count + "Do not proceed to Phase N+1 until GATE [X] is written" | C-16 pass (blocking language), C-17 pass (referenceable named registry); all R2 wins preserved |
| V-02 | phrasing-register | C-15: forbidden-form enumeration | Standing rule enumerates specific forbidden alternatives alongside positive form: "FAIL: 'I found…' / 'This namespace has…'" making the rule self-diagnosing; also adds C-10 tier sourcing | C-15 pass; C-10 gap closed; all R2 wins preserved |
| V-03 | output-format | C-18/C-14: constraint co-location + blank slots | Every fill-in field gets a CONSTRAINT line immediately after it with no intervening prose; all fill-in targets use `___` blank notation visible by inspection | C-18 pass (constraint adjacent, no prose between); C-14 pass (blank slots readable without prose parsing) |
| V-04 | lifecycle-emphasis + phrasing-register | C-16/C-17 + C-15/C-10 | V-01 gate structure + V-02 forbidden-form standing rule + tier sourcing; non-overlapping axes | C-15, C-16, C-17 pass simultaneously; C-10 gap closed; no mutual interference |
| V-05 | lifecycle + phrasing + output-format | C-10 + C-14 + C-15 + C-16 + C-17 + C-18 | Full aspirational stack: tier sourcing, blank slots, forbidden-form rule, written-gate blocking, named gate registry, constraint co-location; all four new criteria + both R2 gaps in one prompt | All 10 aspirational criteria pass; composite >= 95 |

---

## V-01 — Lifecycle Emphasis: Named Gate Registry with Written Blocking

**axis:** lifecycle-emphasis
**hypothesis:** The R2 baseline has phase exit assertions (C-13) but they are narrative — prose
statements that describe what must happen rather than blocking output records. Renaming all
transitions as structured GATE A–F assertions with "Do not proceed to Phase N+1 until GATE [X]
is written" converts soft phase exits into committed output gates. This satisfies C-16 (blocking
language) and C-17 (named, referenceable registry) simultaneously because the gate IDs can be
cited from the review artifact. Failure condition: if model treats gate output as optional prose,
C-16 may pass at the instruction level while C-16's "committed text" requirement fails in
practice — look for gate output in the actual response to distinguish.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
Every auto-flag output and role evaluation uses artifact-as-subject form:
  PASS: "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL: "I found…" / "This namespace has…" / "There is no…"
Check your output before each gate. Rewrite any failing line before the gate fires.

---

PHASE 0 — ORIENT

Read the mock artifact. Output:
  Topic: [name]
  Tier: [N] (source: TOPICS.md | --tier | default)
  Namespaces present: [list]
  Namespaces absent: [list]

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  [N present] + [M absent] = [total]. Expected: 9.
  If total ≠ 9, halt and report discrepancy.
  Do not proceed to Phase 1 until GATE A is written.

---

PHASE 1 — AUTO-FLAG

Three rules. All mandatory. Use artifact-as-subject form throughout.

Rule A (namespace-level):
  For each absent namespace:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level):
  For each present namespace with no mock values:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level):
  For each present namespace lacking a Status field:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three rules:
  "Rule A (namespace-level): [N] / Rule B (artifact-level): [N] / Rule C (evaluation-level): [N]."
  A two-of-three set does not satisfy this gate. All three must be assessed.

GATE B — AUTO-FLAG COMPLETE
  [N namespace-level] + [M artifact-level] + [P evaluation-level] = [total flags].
  Non-flagged namespaces proceeding to evaluation: [9 - total flags].
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.
Initialize: Arch-blocked: []

For each non-auto-flagged namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does structural variance coverage pass?
  SQ: Does the mock artifact's [namespace] section show sufficient structural variance?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
After all: "Arch-blocked: [list] / none"

GATE C — ARCHITECT COMPLETE
  Arch-blocked: [list / none]
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [9 - auto-flagged].
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Evaluate only Architect-ACCEPTED namespaces.
Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does domain knowledge realism pass?
  SQ: Does the mock artifact's [namespace] section reflect domain-realistic values?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
After all: "Strategy-blocked: [list] / none"

GATE D — STRATEGY COMPLETE
  Strategy-blocked: [list / none]
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [Arch MOCK-ACCEPTED count].
  Do not proceed to Phase 4 until GATE D is written.

---

PHASE 4 — STATUS WRITEBACK

Final verdict:
  auto-flagged → REAL-REQUIRED
  Arch-blocked → REAL-REQUIRED
  Strategy-blocked → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace. Write:
  Status: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT

After all edits:
  CANARY ASSERTION: "Status fields written: [N]. Expected: 9. If wrong, writeback is incomplete — do not proceed."
  CANARY-FALSE-POSITIVE: Edit may report success without modifying the file. Verify by rereading the first updated section.
  CANARY SUPPRESSED: If Edit is unavailable, output "CANARY SUPPRESSED — writeback skipped, proceeding to review artifact only."

GATE E — WRITEBACK COMPLETE
  Status fields written: [N]. Expected: 9.
  Do not proceed to Phase 5 until GATE E is written.

---

PHASE 5 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

---
Slot 1 — Reason Code
  Reason: [exact token]
  Constraint: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Revert-on-violation: Any other text — delete and rewrite. Paraphrase is a violation.

---
Slot 2 — Coverage Basis
  Basis: The mock artifact's [namespace] section [shows/records/lacks] [evidence].
  Constraint: Begin "The mock artifact's [namespace] section…"
  Revert-on-violation: Any evaluator-as-subject form — delete and rewrite. Paraphrase is a violation.

---

PHASE 6 — REVIEW ARTIFACT

Write all sections in ONE Write call. No sections outside this Write block.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Section 1: Coverage table (4 cols: Namespace | Auto-flag | Role Verdict | Final Status)
  Section 2: Structural records (one sentence per namespace, artifact-as-subject form)
  Section 3: Risk (Namespace | Risk | Urgency: HIGH / MEDIUM / LOW)
  Section 4: Next Steps (ordered list: namespace · blocking reason · required action)

GATE F — REVIEW ARTIFACT WRITTEN
  Filename confirmed: simulations/mock/review/{topic}-mock-accept-{date}.md
  All four sections present in the Write call.
  Do not claim completion until GATE F is written.

---

## V-02 — Phrasing Register: Forbidden-Form Enumeration in Standing Rule

**axis:** phrasing-register
**hypothesis:** The R2 baseline's standing rule states the positive form ("artifact-as-subject")
but does not name specific forbidden alternatives. A model executing the rule must infer what
counts as a violation. Promoting the forbidden forms to explicit named examples alongside the
positive form — "FAIL: 'I found…' / 'This namespace has…'" — makes the rule self-diagnosing:
any line beginning with a forbidden form is immediately recognizable as a violation without
inference. C-15 pass is predicted because the forbidden alternatives appear verbatim in the
rule. This variation also adds tier sourcing (C-10 gap fix from R2) as a correction-only change.
Failure condition: if the model still produces forbidden-form lines, C-09/C-15 compliance may
require structural enforcement (moving rule to every phase header) rather than phrasing alone.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
Every auto-flag output and role evaluation uses artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

The FAIL forms are forbidden. If your output contains a forbidden form, halt and rewrite
before advancing. No downstream phase output resolves an upstream forbidden form.

---

PHASE 0 — ORIENT

Read the mock artifact. Output:
  Topic: [name]
  Tier: [N] (source: TOPICS.md | --tier | default)
  Namespaces present: [list]
  Namespaces absent: [list]
  Count: [N present] + [M absent] = [total]. Expected: 9. Halt if total ≠ 9.

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

PHASE 1 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation.

Rule A (namespace-level):
  For each absent namespace:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level):
  For each present namespace with no mock values:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level):
  For each present namespace lacking a Status field:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three:
  "Rule A (namespace-level): [N] / Rule B (artifact-level): [N] / Rule C (evaluation-level): [N]."
  A two-of-three set does not satisfy this gate. All three must be assessed.

Completeness check: [N namespace-level] + [M artifact-level] + [P evaluation-level] = [total flags].
Non-flagged namespaces proceeding to evaluation: [9 - total flags].

PHASE 1 EXIT ASSERTION: Auto-flag complete. Forbidden triad verified (3 of 3 labels present).
Do not proceed to Phase 2 until partition is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage.
Initialize: Arch-blocked: []

For each non-auto-flagged namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does structural variance coverage pass?
  SQ: Does the mock artifact's [namespace] section show sufficient structural variance?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
After all: "Arch-blocked: [list] / none"
Partition: "[N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [9 - auto-flagged]."

PHASE 2 EXIT ASSERTION: Architect complete. Arch-blocked list finalized. Partition written.
Do not proceed to Phase 3 until partition is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Only Architect-ACCEPTED namespaces.
Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does domain knowledge realism pass?
  SQ: Does the mock artifact's [namespace] section reflect domain-realistic values?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
After all: "Strategy-blocked: [list] / none"
Partition: "[N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [Arch MOCK-ACCEPTED count]."

PHASE 3 EXIT ASSERTION: Strategy complete. Strategy-blocked list finalized. Partition written.
Do not proceed to Phase 4 until partition is written.

---

PHASE 4 — STATUS WRITEBACK

Final verdict:
  auto-flagged → REAL-REQUIRED
  Arch-blocked → REAL-REQUIRED
  Strategy-blocked → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT

After all edits:
  CANARY ASSERTION: "Status fields written: [N]. Expected: 9. If wrong, writeback is incomplete — do not proceed."
  CANARY-FALSE-POSITIVE: Verify by rereading the first updated section.
  CANARY SUPPRESSED: If Edit unavailable, output "CANARY SUPPRESSED — writeback skipped."

---

PHASE 5 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each MOCK-ACCEPTED namespace, complete both slots.
Both required. Do not merge. Paraphrase is a violation.

Slot 1 — Reason Code
  Reason: [exact token]
  Constraint: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Revert-on-violation: Paraphrase ("sufficient coverage", "domain realistic") — delete and rewrite.

Slot 2 — Coverage Basis
  Basis: The mock artifact's [namespace] section [shows/records/lacks] [evidence].
  Constraint: Begin "The mock artifact's [namespace] section…"
  Revert-on-violation: Forbidden form ("I found…", "Coverage shows…") — delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Coverage table (Namespace | Auto-flag | Role Verdict | Final Status)
  Structural records (one sentence per namespace, artifact-as-subject form)
  Risk (Namespace | Risk | Urgency: HIGH / MEDIUM / LOW)
  Next Steps (ordered list: namespace · blocking reason · required action)

---

## V-03 — Output Format: Constraint-Field Co-Location with Blank Slots

**axis:** output-format
**hypothesis:** The R2 baseline places constraints in preamble sections (e.g., "all reason codes
must be exact tokens" as a preamble instruction, then templates below with no constraint nearby).
A reader executing the template step-by-step can fill in Reason: without re-reading the preamble
constraint. Moving each constraint to immediately after its fill-in field — with no intervening
prose, headers, or instructions — closes C-18 (co-location) because the constraint is physically
adjacent to its target. Simultaneously, converting all fill-in targets to `___` blank notation
closes C-14 (blank-line failure signal) because incomplete slots are structurally visible without
prose parsing. Failure condition: if model ignores inline CONSTRAINT lines and reverts to
preamble-compliance behavior, C-18 and C-14 may still fail — that would indicate the enforcement
mechanism needs to move upstream (e.g., add a CONSTRAINT at every gate).

---

You are running /mock:accept.

STANDING RULE
All auto-flag outputs and role evaluations use artifact-as-subject form:
  PASS: "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL: "I found…" / "This namespace has…" / "There is no…"

---

PHASE 0 — ORIENT

Read the mock artifact and complete:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write "Tier: N (source: TOPICS.md | --tier | default)" with the exact source label.
  Namespaces present: ___
  Namespaces absent: ___
  Count: ___ present + ___ absent = ___
  CONSTRAINT: Expected 9. Halt if count ≠ 9 and report the discrepancy.

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

PHASE 1 — AUTO-FLAG

Three rules. All mandatory.

Rule A — Namespace-level: For each absent namespace, complete:
  Flag: ___
  CONSTRAINT: Write "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B — Artifact-level: For each present namespace with no mock values, complete:
  Flag: ___
  CONSTRAINT: Write "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C — Evaluation-level: For each present namespace lacking a Status field, complete:
  Flag: ___
  CONSTRAINT: Write "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three rules:
  Rule A count: ___
  Rule B count: ___
  Rule C count: ___
  CONSTRAINT: All three lines are required. Two-of-three does not satisfy this gate.
  Completeness: ___ + ___ + ___ = ___ flags total.
  CONSTRAINT: Non-flagged count must equal 9 - total flags.

PHASE 1 EXIT ASSERTION: Auto-flag complete. Partition confirmed.
Do not proceed to Phase 2 until exit assertion is written.

---

PHASE 2 — ARCHITECT EVALUATION

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
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
  Partition: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total equals [9 - auto-flagged].

PHASE 2 EXIT ASSERTION: Architect partition complete.
Do not proceed to Phase 3 until exit assertion is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate only Architect-ACCEPTED namespaces.

For each Architect-ACCEPTED namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
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
  Partition: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total equals Arch MOCK-ACCEPTED count.

PHASE 3 EXIT ASSERTION: Strategy partition complete.
Do not proceed to Phase 4 until exit assertion is written.

---

PHASE 4 — STATUS WRITEBACK

Final verdict:
  auto-flagged → REAL-REQUIRED
  Arch-blocked → REAL-REQUIRED
  Strategy-blocked → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: ___
  CONSTRAINT: Write exactly MOCK-ACCEPTED or REAL-REQUIRED.
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.

After all edits:
  CANARY ASSERTION: Status fields written: ___. Expected: 9.
  CONSTRAINT: If count ≠ 9, writeback is incomplete — do not proceed.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped."

---

PHASE 5 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each MOCK-ACCEPTED namespace, complete both slots. Do not merge slots.
Paraphrase is a violation in both slots.

--- Slot 1 ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Revert-on-violation: "sufficient coverage" / "domain realistic" / "domain consistent" are paraphrase violations. Delete and rewrite.

--- Slot 2 ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" in artifact-as-subject form.
  Revert-on-violation: "I found…" / "Coverage includes…" / "This namespace…" are Slot 2 violations. Delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md

  Section 1: Coverage table
  CONSTRAINT: 4 columns — Namespace | Auto-flag | Role Verdict | Final Status
  Section 2: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form.
  Section 3: Risk table
  CONSTRAINT: Namespace | Risk | Urgency — urgency labels required (HIGH / MEDIUM / LOW).
  Section 4: Next Steps
  CONSTRAINT: Ordered list with namespace · blocking reason · required action per entry.

---

## V-04 — Combined: Lifecycle Emphasis + Phrasing Register (C-16/C-17 + C-15/C-10)

**axis:** lifecycle-emphasis + phrasing-register
**hypothesis:** V-01 (gate registry) and V-02 (forbidden-form enumeration) target structurally
non-overlapping surfaces: V-01 restructures phase transitions, V-02 restructures the standing
rule. Combining them should yield C-15 + C-16 + C-17 simultaneously without mutual interference.
The V-02 tier sourcing correction closes C-10 as well. Expected composite gain: four aspirational
criteria in one variation (C-10, C-15, C-16, C-17). The risk is prompt length: combining both
axes increases word count; if the model begins skipping sections under token pressure, gate
blocking language (C-16) becomes the first defense. Failure condition: if only C-16 or C-17
passes but not C-15, the standing rule phrasing is the remaining gap — extract to V-05 only.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
Every auto-flag output and role evaluation uses artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If output contains a forbidden form, halt and rewrite
before advancing. The rule is active throughout all phases.

---

PHASE 0 — ORIENT

Read the mock artifact. Output:
  Topic: [name]
  Tier: [N] (source: TOPICS.md | --tier | default)
  Namespaces present: [list]
  Namespaces absent: [list]

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  [N present] + [M absent] = [total]. Expected: 9.
  If total ≠ 9, halt and report discrepancy.
  Do not proceed to Phase 1 until GATE A is written.

---

PHASE 1 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout.

Rule A (namespace-level):
  For each absent namespace:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level):
  For each present namespace with no mock values:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level):
  For each present namespace lacking a Status field:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three:
  "Rule A (namespace-level): [N] / Rule B (artifact-level): [N] / Rule C (evaluation-level): [N]."
  A two-of-three set does not satisfy this gate. All three must be assessed.

GATE B — AUTO-FLAG COMPLETE
  [N namespace-level] + [M artifact-level] + [P evaluation-level] = [total flags].
  Non-flagged namespaces proceeding to evaluation: [9 - total flags].
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.
Initialize: Arch-blocked: []

For each non-auto-flagged namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does structural variance coverage pass?
  SQ: Does the mock artifact's [namespace] section show sufficient structural variance?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Arch-blocked: [namespace] added."
After all: "Arch-blocked: [list] / none"

GATE C — ARCHITECT COMPLETE
  Arch-blocked: [list / none]
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [9 - auto-flagged].
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Only Architect-ACCEPTED namespaces.
Initialize: Strategy-blocked: []

For each Architect-ACCEPTED namespace, produce:
  Namespace: [name]
  Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]
  Trigger condition: Does domain knowledge realism pass?
  SQ: Does the mock artifact's [namespace] section reflect domain-realistic values?
  Artifact state: The mock artifact's [namespace] section [records / shows / lacks] [specific detail].
  Verdict: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
  Required action: [specific action if REAL-REQUIRED; "none" if MOCK-ACCEPTED]

VERDICT-ECHO: Each REAL-REQUIRED → "Strategy-blocked: [namespace] added."
After all: "Strategy-blocked: [list] / none"

GATE D — STRATEGY COMPLETE
  Strategy-blocked: [list / none]
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [Arch MOCK-ACCEPTED count].
  Do not proceed to Phase 4 until GATE D is written.

---

PHASE 4 — STATUS WRITEBACK

Final verdict:
  auto-flagged → REAL-REQUIRED
  Arch-blocked → REAL-REQUIRED
  Strategy-blocked → REAL-REQUIRED
  all others → MOCK-ACCEPTED

Use Edit tool for each namespace:
  Status: MOCK-ACCEPTED | REAL-REQUIRED
  Reason: STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT

After all edits:
  CANARY ASSERTION: "Status fields written: [N]. Expected: 9. If wrong, writeback is incomplete — do not proceed."
  CANARY-FALSE-POSITIVE: Verify by rereading the first updated section.
  CANARY SUPPRESSED: If Edit unavailable, output "CANARY SUPPRESSED — writeback skipped."

GATE E — WRITEBACK COMPLETE
  Status fields written: [N]. Expected: 9.
  Do not proceed to Phase 5 until GATE E is written.

---

PHASE 5 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each MOCK-ACCEPTED namespace, complete both slots.
Both required. Do not merge. Paraphrase is a violation in both slots.

---
Slot 1 — Reason Code
  Reason: [exact token]
  Constraint: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Revert-on-violation: Paraphrase ("sufficient coverage", "domain realistic") — delete and rewrite.

---
Slot 2 — Coverage Basis
  Basis: The mock artifact's [namespace] section [shows/records/lacks] [evidence].
  Constraint: Begin "The mock artifact's [namespace] section…"
  Revert-on-violation: Forbidden form ("I found…", "Coverage shows…") — delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Coverage table (Namespace | Auto-flag | Role Verdict | Final Status)
  Structural records (one sentence per namespace, artifact-as-subject form)
  Risk (Namespace | Risk | Urgency: HIGH / MEDIUM / LOW)
  Next Steps (ordered list: namespace · blocking reason · required action)

GATE F — REVIEW ARTIFACT WRITTEN
  Filename confirmed: simulations/mock/review/{topic}-mock-accept-{date}.md
  All four sections present in the Write call.
  Do not claim completion until GATE F is written.

---

## V-05 — Full Integration: All New Criteria (C-10, C-14, C-15, C-16, C-17, C-18)

**axis:** lifecycle-emphasis + phrasing-register + output-format
**hypothesis:** Full aspirational stack test. Four new criteria from rubric v3 plus both R2
gaps in a single variation. C-15 via forbidden-form FAIL examples in the standing rule.
C-16 via "Do not proceed to Phase N+1 until GATE [X] is written" on every gate. C-17 via
GATE A–F stable named registry (referenceable from the review artifact — review artifact
cites "GATE C Arch-blocked list" to close the reference loop). C-18 via each constraint
block placed physically adjacent to its field with no intervening prose, headers, or
instructions. C-10 via tier sourcing output in Phase 0. C-14 via `___` blank slots for
all fill-in targets. If this achieves >= 95 on all criteria, no R4 needed. The testable
failure prediction: C-18 is the hardest new criterion because it requires discipline in
every field across every phase — a single preamble-only constraint anywhere in the prompt
is a C-18 violation. Look for any constraint not immediately adjacent to its field.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. Encountering one is a standing rule violation — halt and
rewrite before advancing to the next gate. The rule is active in every phase.

---

PHASE 0 — ORIENT

Read the mock artifact and write:
  Topic: ___
  Tier: ___
  CONSTRAINT: Write exactly "Tier: N (source: TOPICS.md | --tier | default)" with the source label.
  Namespaces present: ___
  Namespaces absent: ___

9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

GATE A — ORIENT COMPLETE
  Count: ___ present + ___ absent = ___. Expected: 9.
  CONSTRAINT: If count ≠ 9, halt and report the discrepancy before advancing.
  Do not proceed to Phase 1 until GATE A is written.

---

PHASE 1 — AUTO-FLAG

Three rules. All mandatory. Artifact-as-subject form throughout.

Rule A (namespace-level): For each absent namespace, write:
  "The mock artifact's [ns] section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's [ns] section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's [ns] section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three rules:
  Rule counts: ___ namespace-level / ___ artifact-level / ___ evaluation-level
  CONSTRAINT: All three lines required. Two-of-three does not satisfy this gate.

GATE B — AUTO-FLAG COMPLETE
  Total flags: ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___
  CONSTRAINT: Non-flagged count must equal 9 - total flags.
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  Trigger condition: ___
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
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [9 - auto-flagged].
  CONSTRAINT: Arch-blocked list is now closed. Do not add to it after this gate.
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.

For each Architect-ACCEPTED namespace (see GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim.
  Trigger condition: ___
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
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [GATE C Arch MOCK-ACCEPTED count].
  CONSTRAINT: Strategy-blocked list is now closed.
  Do not proceed to Phase 4 until GATE D is written.

---

PHASE 4 — STATUS WRITEBACK

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
  CONSTRAINT: If count ≠ 9, writeback is incomplete — do not proceed.
  CANARY-FALSE-POSITIVE: ___
  CONSTRAINT: Verify by rereading the first modified section and confirming the value changed.
  CANARY SUPPRESSED: If Edit unavailable, write "CANARY SUPPRESSED — writeback skipped."

GATE E — WRITEBACK COMPLETE
  Status fields written: ___. Expected: 9.
  CONSTRAINT: CANARY ASSERTION must be written before this gate fires.
  Do not proceed to Phase 5 until GATE E is written.

---

PHASE 5 — MOCK-ACCEPTED POSITIVE ARGUMENT

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both slots required. Do not merge. Paraphrase is a violation in both slots.

--- Slot 1 ---
  Reason: ___
  CONSTRAINT: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT. No other text.
  Revert-on-violation: "sufficient coverage" / "domain realistic" / "domain consistent" are paraphrase violations. Delete and rewrite with the exact token.

--- Slot 2 ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject form required.
  Revert-on-violation: "I found…" / "Coverage includes…" / "This namespace…" are Slot 2 violations. Delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md

  Section 1: Coverage table
  CONSTRAINT: 4 columns: Namespace | Auto-flag | Role Verdict | Final Status
  Section 2: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form; reference GATE C and GATE D lists where relevant.
  Section 3: Risk
  CONSTRAINT: Namespace | Risk | Urgency — urgency labels required: HIGH / MEDIUM / LOW.
  Section 4: Next Steps
  CONSTRAINT: Ordered list with namespace · blocking reason · required action per entry.

GATE F — REVIEW ARTIFACT WRITTEN
  Filename confirmed: simulations/mock/review/{topic}-mock-accept-{date}.md
  CONSTRAINT: All four sections present in Write call; no section outside Write block.
  Do not claim completion until GATE F is written.

---

## Axis Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-10 Tier sourcing | + | + | + | + | + |
| C-14 Blank-line failure signal | — | — | + | — | + |
| C-15 Forbidden-form enumeration | — | + | — | + | + |
| C-16 Written-gate blocking language | + | — | — | + | + |
| C-17 Named gate registry | + | — | — | + | + |
| C-18 Constraint-field co-location | — | — | + | — | + |
| R2 baseline (C-09/C-11/C-12/C-13) | all | all | all | all | all |

Single-axis predictions: V-01 adds C-16+C-17 · V-02 adds C-10+C-15 · V-03 adds C-14+C-18
Combination predictions: V-04 adds C-10+C-15+C-16+C-17 · V-05 adds all six

```json
{"round": 3, "rubric_version": "v3-revised", "new_criteria": ["C-15", "C-16", "C-17", "C-18"], "gap_fixes": ["C-10", "C-14"], "r2_baseline_passes": ["C-09", "C-11", "C-12", "C-13"], "predicted_ceiling": {"V-01": "88.0", "V-02": "88.0", "V-03": "88.0", "V-04": "94.0", "V-05": "100.0"}}
```
