Now I have the full picture. Generating all 5 variations:

---

# mock-accept Variate — Round 4 (rubric v4)

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v4 (C-01–C-05 essential; C-06–C-08 recommended; C-09–C-22 aspirational; C-19–C-22 new this round)
**Baseline:** R3 champion — V-04 at 98.0 (passes C-09/C-10/C-11/C-12/C-13/C-15/C-16/C-17; fails C-14/C-18; new C-19–C-22 unscored)
**Round:** R4 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R3 converged on GATE A–F registry (C-16/C-17), forbidden-form enumeration (C-15), and tier sourcing (C-10). V-04 carries all of these forward. The two persistent failures are C-14 (bracket notation instead of `___` blanks) and C-18 (Phase 2/3 constraints embedded inline rather than framed adjacent blocks). V-03/V-05 from R3 fixed both but dropped the SQ field and lost C-08. R4 targets the four new criteria plus those two failures, with explicit SQ preservation as a cross-cutting constraint.

| Plan | Axis | Source criterion | What changes | Predicted |
|------|------|-----------------|--------------|-----------|
| V-01 | output-format | C-14/C-18/C-19: blank-slot + constraint co-location | All `[bracket]` fill-ins → `___`; framed CONSTRAINT: block after every constrained field in Phases 0–5; auto-flag rule templates use `___` for namespace slot; CANARY ASSERTION uses `___` for count; SQ field **explicitly retained** with its own `___` + CONSTRAINT to prevent C-08 collapse | C-14 pass (blank slots throughout), C-18 pass (adjacent CONSTRAINT blocks in Phases 2/3/4), C-19 pass (universal blank-slot in auto-flag templates + CANARY); C-08 preserved by explicit SQ retention |
| V-02 | lifecycle-emphasis | C-21: per-section review artifact structure | Phase 6 gains per-section CONSTRAINT blocks immediately after each section name; GATE F cites specific section IDs; Phases 0–5 unchanged from V-04; `[bracket]` notation kept | C-21 pass (each section carries co-located CONSTRAINT); C-08 preserved (Phase 2/3 unchanged); no blank-slot changes so C-14/C-18/C-19 remain gaps |
| V-03 | phrasing-register | C-20/C-22: halt naming + paraphrase examples | Standing rule halt rewritten as named action sequence: "HALT. Delete the violating line. Rewrite in PASS form."; Slot 1 revert gains third concrete example ("coverage sufficient"); Slot 2 revert shifts from forbidden-form labeling to near-miss paraphrase examples | C-20 unambiguous pass (explicit HALT + delete + rewrite action sequence); C-22 unambiguous pass (three Slot-1 examples, two near-miss Slot-2 examples); C-14/C-18/C-21 remain gaps |
| V-04 | output-format + lifecycle-emphasis | C-14/C-18/C-19 + C-21 | V-01 blank-slot structure across Phases 0–5 + V-02 per-section Phase 6 CONSTRAINTs; non-overlapping surfaces | C-14/C-18/C-19/C-21 pass simultaneously; C-08 preserved; V-03 phrasing not included |
| V-05 | output-format + lifecycle + phrasing-register | All 4 new criteria + C-14/C-18 | Full stack: V-04 structure + V-03's HALT language and extended paraphrase examples; all axes in one prompt | C-14/C-18/C-19/C-20/C-21/C-22 pass; aspirational denominator 14/14; composite target 100 |

---

## V-01 — Output Format: Universal Blank-Slot Enforcement + Constraint Co-location

**axis:** output-format
**hypothesis:** R3 V-04 champion uses `[bracket]` notation for every fill-in target and embeds role-evaluation constraints inline within template phrasing (no separate framed CONSTRAINT blocks in Phases 2/3). Two gaps remain: C-14 requires structurally visible blank slots readable without prose parsing; C-18 requires each constraint block to be co-located with its field with no intervening prose. A third gap — C-19 — requires that the *auto-flag rule output templates* and the *CANARY ASSERTION count slot* also use `___` notation, not bracket placeholders. V-01 addresses all three by (1) converting every fill-in to `___`, (2) adding a framed `CONSTRAINT:` line immediately after each constrained field in all phases, and (3) applying `___` to Rule A/B/C output templates and the CANARY slot. The critical design constraint: R3 V-03 and V-05 both added blank-slot + CONSTRAINT-per-field and both dropped the SQ field, losing C-08. V-01 explicitly retains SQ as a labeled field with its own `___` + `CONSTRAINT:` to prevent this collapse. Failure mode: if the model treats the SQ CONSTRAINT as redundant alongside Artifact state CONSTRAINT and collapses them, C-08 fails — look for a distinct SQ line in the actual response to distinguish.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If output contains a forbidden form, halt and rewrite
before advancing. The rule is active in every phase.

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
  "The mock artifact's ___ section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's ___ section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's ___ section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three:
  Rule A (namespace-level): ___
  Rule B (artifact-level): ___
  Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.

GATE B — AUTO-FLAG COMPLETE
  ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ flags total.
  CONSTRAINT: Non-flagged count must equal 9 - total flags.
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section show sufficient structural variance?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [9 - auto-flagged].
  CONSTRAINT: Arch-blocked list is now closed. Do not add to it after this gate.
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.

For each Architect-ACCEPTED namespace (see GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section reflect domain-realistic values?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [GATE C Arch MOCK-ACCEPTED count].
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

After all edits:
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
  Revert-on-violation: Paraphrase ("sufficient coverage", "domain realistic") — delete and rewrite with the exact token.

--- Slot 2 ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject form required.
  Revert-on-violation: Forbidden form ("I found…", "Coverage shows…") — delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
Filename: simulations/mock/review/{topic}-mock-accept-{date}.md

  Coverage table (Namespace | Auto-flag | Role Verdict | Final Status)
  Structural records (one sentence per namespace, artifact-as-subject form; reference GATE C and GATE D lists)
  Risk (Namespace | Risk | Urgency: HIGH / MEDIUM / LOW)
  Next Steps (ordered list: namespace · blocking reason · required action)

GATE F — REVIEW ARTIFACT WRITTEN
  Filename confirmed: simulations/mock/review/{topic}-mock-accept-{date}.md
  All four sections present in the Write call.
  Do not claim completion until GATE F is written.

---

## V-02 — Lifecycle Emphasis: Per-Section CONSTRAINT in Review Write Block

**axis:** lifecycle-emphasis
**hypothesis:** R3 V-04 champion's Phase 6 lists four sections with brief prose descriptors but carries no co-located CONSTRAINT block for each section name. C-21 requires each named section within the review artifact Write block to carry its own CONSTRAINT block — a structural property first demonstrated by V-03 from R3 (which scored C-04 PASS with "4 sections with CONSTRAINT per section"). V-02 grafts this pattern onto V-04 without touching Phases 0–5: no blank-slot changes, no standing rule changes, no SQ field changes. This isolates C-21 as the single-axis target. Additionally, GATE F is expanded to cite each section by ID, converting the review artifact gate from a single completeness check into a section-level registry. This also strengthens C-17's reference loop: when GATE F explicitly names Section 1 through Section 4, those names become referenceable IDs. Failure mode: if the model produces the sections with CONSTRAINTs but omits one section entirely (e.g., folds Risk into Next Steps), C-04 may fail while C-21 nominally passes — verify that all four sections appear as distinct named blocks.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If output contains a forbidden form, halt and rewrite
before advancing. The rule is active in every phase.

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

For each Architect-ACCEPTED namespace (see GATE C), produce:
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
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [GATE C Arch MOCK-ACCEPTED count].
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

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
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

  Section 1: Coverage table
  CONSTRAINT: 4 columns — Namespace | Auto-flag | Role Verdict | Final Status; one row per namespace.

  Section 2: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form; reference GATE C Arch-blocked and GATE D Strategy-blocked lists where relevant.

  Section 3: Risk
  CONSTRAINT: Namespace | Risk | Urgency — urgency labels required: HIGH / MEDIUM / LOW; every row must carry a label.

  Section 4: Next Steps
  CONSTRAINT: Ordered list; each entry: namespace · blocking reason · required action; omit MOCK-ACCEPTED namespaces with no action required.

GATE F — REVIEW ARTIFACT WRITTEN
  Sections confirmed: Section 1 (Coverage table) + Section 2 (Structural records) + Section 3 (Risk) + Section 4 (Next Steps) — all present in Write call.
  All four sections inside the Write block; no section written outside.
  Do not claim completion until GATE F is written.

---

## V-03 — Phrasing Register: Halt-Action Naming + Concrete Paraphrase Examples

**axis:** phrasing-register
**hypothesis:** R3 V-04's standing rule writes "halt and rewrite before advancing" — conditional phrasing that names the action but buries it in an if-clause. C-20 requires an explicit halt or stop instruction *naming the action to take*; V-04 may pass C-20 on a lenient read but fails on a strict reading that demands the halt stand as an imperative, not a conditional. V-03 restructures the violation response as a three-step named sequence: HALT (stop output), DELETE (identify and remove the violating line), REWRITE (produce the PASS form before continuing). This is unconditional imperative, not conditional prose. For C-22, V-04 already carries two Slot-1 paraphrase examples ("sufficient coverage", "domain realistic") and two Slot-2 forbidden-form examples. V-03 strengthens Slot 1 to three near-miss examples and restructures Slot 2 to focus on *paraphrase near-misses* of the artifact-as-subject form (altered-token violations that look almost right) rather than the outright forbidden forms already covered by the standing rule. Failure mode: if the model applies the three-step halt to every output line (not just violations), the prompt becomes self-interrupting — look for the halt appearing only in violation correction context.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Do not write the next line.
  DELETE the violating line from your output.
  REWRITE it in PASS form before continuing.
The rule is active in every phase. No gate fires over an unresolved violation.

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

For each Architect-ACCEPTED namespace (see GATE C), produce:
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
  [N MOCK-ACCEPTED] + [M REAL-REQUIRED] = [total]. Expected: [GATE C Arch MOCK-ACCEPTED count].
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

For each namespace with final verdict MOCK-ACCEPTED, complete both slots.
Both required. Do not merge. Paraphrase is a violation in both slots.

---
Slot 1 — Reason Code
  Reason: [exact token]
  Constraint: Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT.
  Revert-on-violation: The following are paraphrase violations — delete and rewrite the exact token:
    "sufficient coverage" / "coverage sufficient" / "domain realistic"

---
Slot 2 — Coverage Basis
  Basis: The mock artifact's [namespace] section [shows/records/lacks] [evidence].
  Constraint: Begin "The mock artifact's [namespace] section…" — artifact-as-subject form required.
  Revert-on-violation: The following are near-miss paraphrase violations — delete and rewrite:
    "The mock [namespace] section…" (missing "artifact's")
    "The artifact's [namespace] section…" (missing "mock")

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

## V-04 — Combined: Output Format + Lifecycle Emphasis (C-14/C-18/C-19 + C-21)

**axis:** output-format + lifecycle-emphasis
**hypothesis:** V-01 (blank-slot + CONSTRAINT co-location across Phases 0–5) and V-02 (per-section CONSTRAINT in Phase 6) target structurally non-overlapping surfaces: Phases 0–5 template fields vs. Phase 6 section headers. Combining them should yield C-14/C-18/C-19/C-21 simultaneously with no mutual interference. The risk is Phase 6 CONSTRAINT density: adding both per-section CONSTRAINTs (V-02) and the blank-slot `___` for the filename (V-01) in the same phase increases structural load. If this causes the model to omit a section body while writing its CONSTRAINT, C-04 may fail locally even if C-21 passes formally. GATE F is expanded to name all four sections explicitly — if a section is absent, it appears missing from the GATE F checklist. The V-01 SQ retention fix carries forward unchanged into V-04 as the primary C-08 protection.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If output contains a forbidden form, halt and rewrite
before advancing. The rule is active in every phase.

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
  "The mock artifact's ___ section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's ___ section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's ___ section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three:
  Rule A (namespace-level): ___
  Rule B (artifact-level): ___
  Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.

GATE B — AUTO-FLAG COMPLETE
  ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ flags total.
  CONSTRAINT: Non-flagged count must equal 9 - total flags.
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section show sufficient structural variance?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [9 - auto-flagged].
  CONSTRAINT: Arch-blocked list is now closed. Do not add to it after this gate.
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.

For each Architect-ACCEPTED namespace (see GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section reflect domain-realistic values?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [GATE C Arch MOCK-ACCEPTED count].
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

After all edits:
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
  Revert-on-violation: Paraphrase ("sufficient coverage", "domain realistic") — delete and rewrite with the exact token.

--- Slot 2 ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject form required.
  Revert-on-violation: Forbidden form ("I found…", "Coverage shows…") — delete and rewrite.

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md

  Section 1: Coverage table
  CONSTRAINT: 4 columns — Namespace | Auto-flag | Role Verdict | Final Status; one row per namespace.

  Section 2: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form; reference GATE C Arch-blocked and GATE D Strategy-blocked lists where relevant.

  Section 3: Risk
  CONSTRAINT: Namespace | Risk | Urgency — urgency labels required: HIGH / MEDIUM / LOW; every row must carry a label.

  Section 4: Next Steps
  CONSTRAINT: Ordered list; each entry: namespace · blocking reason · required action; omit MOCK-ACCEPTED namespaces with no action required.

GATE F — REVIEW ARTIFACT WRITTEN
  Sections confirmed: Section 1 (Coverage table) + Section 2 (Structural records) + Section 3 (Risk) + Section 4 (Next Steps) — all present.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  CONSTRAINT: All four sections inside Write block; no section written outside.
  Do not claim completion until GATE F is written.

---

## V-05 — Full Integration: All New Criteria (C-14/C-18/C-19/C-20/C-21/C-22)

**axis:** output-format + lifecycle-emphasis + phrasing-register
**hypothesis:** Full aspirational stack under rubric v4. V-04's blank-slot structure (C-14/C-18/C-19) plus per-section Phase 6 CONSTRAINTs (C-21) plus V-03's HALT action sequence (C-20) and extended near-miss paraphrase examples (C-22) — all four axes in one prompt. The primary risk is the same C-08 SQ collapse that defeated R3 V-03 and V-05: the CONSTRAINT-per-field density in Phases 2/3 creates design pressure to drop SQ. V-05 counters this with an **explicit SQ retention note** at the Phase 2 header — "SQ field is required; do not collapse into Artifact state" — making the anti-collapse rule explicit rather than structural. Secondary risk: GATE F now carries both per-section CONSTRAINTs (C-21) and the `___` filename slot (C-14/C-19) together; if the model omits the filename blank in GATE F, C-19 fails locally. Verify all `___` slots are populated in the actual response output. Predicted composite: 60 + 30 + (14/14)×10 = 100, contingent on SQ retention.

---

You are running /mock:accept.

STANDING RULE — Artifact-as-Subject
All auto-flag outputs and role evaluations use artifact-as-subject form.

  PASS form:  "The mock artifact's [namespace] section [shows / records / lacks]…"
  FAIL forms: "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"

These FAIL forms are forbidden. If your output contains a forbidden form:
  HALT. Do not write the next line.
  DELETE the violating line from your output.
  REWRITE it in PASS form before continuing.
The rule is active in every phase. No gate fires over an unresolved violation.

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
  "The mock artifact's ___ section is absent. AUTO-FLAG: REAL-REQUIRED (namespace-level)."

Rule B (artifact-level): For each present namespace with no mock values, write:
  "The mock artifact's ___ section records no mock values. AUTO-FLAG: REAL-REQUIRED (artifact-level)."

Rule C (evaluation-level): For each present namespace lacking a Status field, write:
  "The mock artifact's ___ section lacks a Status field. AUTO-FLAG: REAL-REQUIRED (evaluation-level)."

After all three:
  Rule A (namespace-level): ___
  Rule B (artifact-level): ___
  Rule C (evaluation-level): ___
  CONSTRAINT: All three lines required. A two-of-three set does not satisfy this gate.

GATE B — AUTO-FLAG COMPLETE
  ___ namespace-level + ___ artifact-level + ___ evaluation-level = ___ flags total.
  CONSTRAINT: Non-flagged count must equal 9 - total flags.
  Do not proceed to Phase 2 until GATE B is written.

---

PHASE 2 — ARCHITECT EVALUATION

Evaluate structural variance coverage. Populate Arch-blocked as you go.
Note: SQ field is required for each namespace. Do not collapse SQ into Artifact state.

For each non-auto-flagged namespace, complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section show sufficient structural variance?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [9 - auto-flagged].
  CONSTRAINT: Arch-blocked list is now closed. Do not add to it after this gate.
  Do not proceed to Phase 3 until GATE C is written.

---

PHASE 3 — STRATEGY EVALUATION

Evaluate domain knowledge realism. Architect-ACCEPTED namespaces only.
Note: SQ field is required for each namespace. Do not collapse SQ into Artifact state.

For each Architect-ACCEPTED namespace (see GATE C), complete:
  Namespace: ___
  Required artifact citation: ___
  CONSTRAINT: Write "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]."
  Trigger condition: ___
  SQ: ___
  CONSTRAINT: Write "Does the mock artifact's [namespace] section reflect domain-realistic values?"
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
  ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___. Expected: [GATE C Arch MOCK-ACCEPTED count].
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

After all edits:
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
  Revert-on-violation: The following are paraphrase violations — delete and rewrite the exact token:
    "sufficient coverage" / "coverage sufficient" / "domain realistic"

--- Slot 2 ---
  Basis: ___
  CONSTRAINT: Begin "The mock artifact's [namespace] section…" — artifact-as-subject form required.
  Revert-on-violation: The following are near-miss paraphrase violations — delete and rewrite:
    "The mock [namespace] section…" (missing "artifact's")
    "The artifact's [namespace] section…" (missing "mock")

---

PHASE 6 — REVIEW ARTIFACT

All sections in ONE Write call. No orphaned sections.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md

  Section 1: Coverage table
  CONSTRAINT: 4 columns — Namespace | Auto-flag | Role Verdict | Final Status; one row per namespace.

  Section 2: Structural records
  CONSTRAINT: One sentence per namespace in artifact-as-subject form; reference GATE C Arch-blocked and GATE D Strategy-blocked lists where relevant.

  Section 3: Risk
  CONSTRAINT: Namespace | Risk | Urgency — urgency labels required: HIGH / MEDIUM / LOW; every row must carry a label.

  Section 4: Next Steps
  CONSTRAINT: Ordered list; each entry: namespace · blocking reason · required action; omit MOCK-ACCEPTED namespaces with no action required.

GATE F — REVIEW ARTIFACT WRITTEN
  Sections confirmed: Section 1 (Coverage table) + Section 2 (Structural records) + Section 3 (Risk) + Section 4 (Next Steps) — all present.
  Filename: ___
  CONSTRAINT: Must match simulations/mock/review/{topic}-mock-accept-{date}.md
  CONSTRAINT: All four sections inside Write block; no section written outside.
  Do not claim completion until GATE F is written.

---

## Axis Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Artifact-as-subject grammar | + | + | + | + | + |
| C-10 Tier sourcing | + | + | + | + | + |
| C-11 Inline completeness gate | + | + | + | + | + |
| C-12 Reason-code at point of use | + | + | + | + | + |
| C-13 Phase exit assertions | + | + | + | + | + |
| C-14 Blank-line failure signal | **+** | — | — | **+** | **+** |
| C-15 Forbidden-form enumeration | + | + | + | + | + |
| C-16 Written-gate blocking language | + | + | + | + | + |
| C-17 Named gate registry | + | + | + | + | + |
| C-18 Constraint-field co-location | **+** | — | — | **+** | **+** |
| C-19 Universal blank-slot enforcement | **+** | — | — | **+** | **+** |
| C-20 Halt-on-violation instruction | (carry) | (carry) | **+** | (carry) | **+** |
| C-21 Per-section CONSTRAINT in review | — | **+** | — | **+** | **+** |
| C-22 Paraphrase violation examples | (carry) | (carry) | **+** | (carry) | **+** |
| C-08 SQ field preserved | **+** (explicit) | + | + | **+** (explicit) | **+** (explicit + note) |

**+** = targeted by this variation's axis  
(carry) = expected from R3 V-04 baseline without change  
— = intentionally absent from this single-axis variation

Single-axis predictions: V-01 adds C-14/C-18/C-19 · V-02 adds C-21 · V-03 strengthens C-20/C-22  
Combination predictions: V-04 adds C-14/C-18/C-19/C-21 · V-05 adds all six new + R4 ceiling target  

Critical anti-regression: V-01/V-04/V-05 all carry an explicit SQ retention mechanism — labeled field + CONSTRAINT or header note — to prevent the C-08 collapse documented in R3 V-03/V-05.

```json
{"round": 4, "rubric_version": "v4", "new_criteria": ["C-19", "C-20", "C-21", "C-22"], "r3_champion": "V-04 at 98.0", "r3_failures_carried": ["C-14", "C-18"], "baseline_passes_carried": ["C-09", "C-10", "C-11", "C-12", "C-13", "C-15", "C-16", "C-17"], "anti_regression": "SQ field explicit retention in V-01/V-04/V-05 to prevent C-08 collapse", "predicted_ceiling": {"V-01": "98.x (C-14/C-18/C-19 pass; C-21 gap)", "V-02": "98.x (C-21 pass; C-14/C-18/C-19 gap)", "V-03": "98.x (C-20/C-22 strengthened; C-14/C-18/C-19/C-21 gap)", "V-04": "99.x (C-14/C-18/C-19/C-21 pass; C-20/C-22 carry)", "V-05": "100 (all criteria; contingent on SQ retention)"}}
```
