Two excellence signals → two new aspirational criteria: **C-26** (self-referential criterion enforcement) and **C-27** (spine-as-sole-suspenders declaration). Max bumps from 175 → 185.

```markdown
# listen-support Quest Rubric — v8

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |
| v6 | Added C-21 (Evidence-to-gap traceability with orphan-gap check), C-22 (Prohibited sentinel language on consequence fields) from R5 excellence signals. Max: 160 pts |
| v7 | Added C-23 (Belt-and-suspenders criterion satisfaction), C-24 (Materialized-view traceability instruction), C-25 (Criterion-ID-named final verification spine) from R6 excellence signals. Max: 175 pts |
| v8 | Added C-26 (Self-referential criterion enforcement), C-27 (Spine-as-sole-suspenders declaration) from R7 excellence signals. Max: 185 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×19) | 5 | 2 | 0 |

**Max composite:** 185 pts  
**Golden gate:** all_essential_pass = TRUE AND composite ≥ 80

PARTIAL on any Essential criterion = all_essential_pass FALSE (Golden blocked regardless of composite).

---

## Essential Criteria (12 pts each, max 60)

### C-01 — Title field on card
Each ticket card includes `Title: [descriptive subject line]` as a named field. A ticket ID (`Ticket T-NN`) does not satisfy this criterion — Title must be a human-readable subject line that summarizes the feedback. A heading of the form `## T-NN — {Title}` does not satisfy this criterion; the title must appear as a discrete named field in the card body.

**PASS:** Every card has a `Title:` field with a descriptive value.  
**PARTIAL:** Title absent on some cards, or ticket ID used in place of subject line, or title embedded in heading only.  
**FAIL:** No title field on any card.

---

### C-02 — Controlled vocabulary declared and enforced
Phase, Category, Volume, and Severity use controlled vocabularies declared in the planning table. The model enforces values — no free-form variants accepted in scored fields.

**PASS:** Vocabulary table present; all card values match declared options.  
**PARTIAL:** Vocabulary declared but not consistently enforced.  
**FAIL:** Free-form values used; no vocabulary declaration.

---

### C-03 — First-person voice throughout
All ticket bodies written in first person. No role titles in body text. The voice constraint is stated explicitly in the prompt (e.g., "Write as me — first person throughout. No role titles in body text.").

**PASS:** All bodies pass first-person check; constraint is stated in prompt.  
**PARTIAL:** Constraint stated but some bodies break first-person or include role titles.  
**FAIL:** Constraint absent or systematically violated.

---

### C-04 — Gap analysis with three named sections
A gap analysis step (distinct from ticket generation) produces three sections: Doc Gaps, Design Gaps, Operational Gaps. Each section must reference ≥1 named artifact.

**PASS:** All three sections present, each with ≥1 named artifact.  
**PARTIAL:** Sections present but one or more is empty or unnamed.  
**FAIL:** Gap analysis absent or fewer than three sections.

---

### C-05 — Minimum ticket count enforced with structural gate
A TABLE CHECK block appears after the planning table and before ticket generation. The block verifies that declared phase or layer minimums sum to ≥7. An explicit halt instruction names the next step and blocks progression until the check passes (e.g., "Do not proceed to STEP 4 until this check shows YES"). The minimum must be declared structurally, not as an advisory instruction.

**PASS:** TABLE CHECK block present with halt instruction naming the blocked step; minimums sum to ≥7; gate is structural not advisory.  
**PARTIAL:** TABLE CHECK or halt instruction present but minimum is < 7, or enforcement is advisory language without a named gate.  
**FAIL:** No TABLE CHECK, no halt instruction, or no minimum declared.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — [reserved]
### C-07 — [reserved]
### C-08 — [reserved]

---

## Aspirational Criteria (5 pts each, max 95)

### C-09 — [reserved]
### C-10 — [reserved]

---

### C-11 — Phase as named card field
Each ticket card includes `Phase:` as a discrete named field populated from the controlled vocabulary.

**PASS:** Every card has a `Phase:` field with a vocabulary-compliant value.  
**PARTIAL:** Phase field present on some cards but absent or free-form on others.  
**FAIL:** No Phase field on any card.

---

### C-12 — Fallback-grounded severity
Severity values are grounded in fallback availability. The Phase Map or equivalent structure distinguishes between phases where a fallback exists (lower severity floor) and phases where no fallback exists (higher severity floor). The inference rule is stated explicitly.

**PASS:** Phase Map or equivalent table distinguishes fallback-available vs. no-fallback phases with explicit severity inference rule.  
**PARTIAL:** Severity differentiation present but fallback rationale not stated.  
**FAIL:** No fallback-grounded severity differentiation.

---

### C-13 — Mid-output verification block
A TABLE CHECK or equivalent verification block appears between the planning table and ticket generation, not only at the end. This mid-output gate catches planning defects before generation begins.

**PASS:** Verification block present after planning step and before ticket generation step.  
**PARTIAL:** Verification present but positioned after generation rather than before.  
**FAIL:** No mid-output verification block.

---

### C-14 — Phase-differentiated register
The constraint manifest or equivalent structure declares minimum ticket counts per phase, enforcing register differentiation (e.g., discovery-phase tickets ≥ N, operational-phase tickets ≥ M). Phase vocabulary framing appears at the planning step.

**PASS:** Per-phase minimums declared with explicit vocabulary framing at planning step.  
**PARTIAL:** Phase differentiation present but minimums not declared per phase.  
**FAIL:** No phase-differentiated register constraint.

---

### C-15 — Temporal adoption window severity
The Phase Map or equivalent structure includes time-window columns (e.g., "day 0–30", "day 61–90") that ground severity in adoption timeline position.

**PASS:** Time-window columns present in Phase Map; severity is traceable to adoption timeline.  
**PARTIAL:** Time windows referenced in prose but not structurally encoded in Phase Map.  
**FAIL:** No temporal adoption window in severity model.

---

### C-16 — VM Row ID in commitment table
The vocabulary materialization commitment table (STEP 3B or equivalent) includes a VM Row ID column, establishing a stable reference identifier for each vocabulary row before tickets are generated.

**PASS:** VM Row ID column present in commitment table.  
**PARTIAL:** Row IDs present but inconsistently assigned or unnamed.  
**FAIL:** No VM Row ID column.

---

### C-17 — Phase-as-severity-key declaration
The Phase Map or equivalent structure is explicitly declared as a severity-key before the planning table. The declaration states that phase determines the severity inference rule, not vice versa.

**PASS:** Explicit severity-key declaration present before planning table; phase-to-severity inference rule stated in prose.  
**PARTIAL:** Phase-to-severity relationship implied but not declared as a key.  
**FAIL:** No severity-key declaration.

---

### C-18 — Gate minimum correct at ≥7
The TABLE CHECK gate explicitly states the minimum as ≥7 (not merely "match the manifest" or an implicit count). The value 7 appears as a literal threshold in the gate condition.

**PASS:** TABLE CHECK contains explicit "≥7" or "minimum 7" threshold.  
**PARTIAL:** Gate present but threshold is < 7 or not stated as a literal value.  
**FAIL:** No explicit minimum threshold in gate.

---

### C-19 — TABLE CHECK halt names next step
The TABLE CHECK halt instruction names the specific next step that is blocked (e.g., "Do not proceed to STEP 6"). A generic "do not proceed" without naming the blocked step does not satisfy this criterion.

**PASS:** Halt instruction names the blocked step by number or label.  
**PARTIAL:** Halt instruction present but next step not named.  
**FAIL:** No halt instruction.

---

### C-20 — VM Row ID in ticket headline
Each generated ticket's `##` headline includes its VM Row ID, making the vocabulary materialization traceable to the output artifact.

**PASS:** Every ticket `##` headline includes its VM Row ID.  
**PARTIAL:** VM Row ID present in some headlines but absent in others.  
**FAIL:** No VM Row IDs in ticket headlines.

---

### C-21 — Five-item gate with orphan-gap check
The gap analysis gate includes at least five items, with item (e) being an inter-role register differentiation check or equivalent orphan-gap check that confirms every gap maps to a named evidence artifact.

**PASS:** Five gate items present; item (e) is an orphan-gap or inter-role check.  
**PARTIAL:** Gate present with fewer than five items, or item (e) absent.  
**FAIL:** No five-item gate.

---

### C-22 — [reserved]

---

### C-23 — Belt-and-suspenders criterion satisfaction
Each Essential and Recommended criterion is enforced at two levels: a `[C-NN: BELT]` label at the generation step where the criterion is satisfied, and a `[C-NN: SUSPENDERS]` label in the final verification spine where the criterion is confirmed. Both halves must be present — suspenders alone (verification only) or belt alone (generation only) does not satisfy this criterion.

**PASS:** Every scored criterion has a `[C-NN: BELT]` label at its generation step and a `[C-NN: SUSPENDERS]` label in the verification spine.  
**PARTIAL:** Belt labels present without suspenders labels, or suspenders labels present without belt labels.  
**FAIL:** No belt-and-suspenders labeling system present.

---

### C-24 — Materialized-view traceability instruction
The prompt includes a VOCABULARY MATERIALIZATION section with two parts: (1) a materialization table mapping VM Row ID → commitment table row → ticket headline location, and (2) an orphan check verifying both directions (unmaterialized rows and unanchored headlines). The TABLE CHECK gate verifies that Part 1 is complete before ticket generation proceeds.

**PASS:** VOCABULARY MATERIALIZATION section present with both parts; TABLE CHECK references it.  
**PARTIAL:** Materialization table present but orphan check absent, or TABLE CHECK does not verify it.  
**FAIL:** No VOCABULARY MATERIALIZATION section.

---

### C-25 — Criterion-ID-named final verification spine
The final verification step is a CRITERION VERIFICATION SPINE: a table with one row per criterion, columns for C-ID, criterion name, required condition, actual output location, and PASS/PARTIAL/FAIL result. A "SPINE RESULT" declaration closes the spine. A VERIFICATION MANIFEST with named structural checks but no C-ID column does not satisfy this criterion.

**PASS:** CRITERION VERIFICATION SPINE present with C-ID column, one row per criterion, and SPINE RESULT declaration.  
**PARTIAL:** Spine-like structure present but missing C-ID column or SPINE RESULT declaration.  
**FAIL:** No criterion-ID-named spine; VERIFICATION MANIFEST retained as sole verification artifact.

---

### C-26 — Self-referential criterion enforcement
Each criterion that defines a structural mechanism (belt-and-suspenders labeling, vocabulary materialization, verification spine, or any future mechanism-defining criterion) carries its own `[C-NN: BELT]` label in the Compliance Contract, pointing to the step or section that satisfies it. A criterion that defines a mechanism proves the mechanism by being the first thing the mechanism is applied to. C-23 must have `[C-23: BELT]`. C-24 must have `[C-24: BELT]` pointing to the VOCABULARY MATERIALIZATION section. C-25 must have `[C-25: BELT]` pointing to the spine step.

**PASS:** Every mechanism-defining criterion in the Compliance Contract carries its own `[C-NN: BELT]` label with a pointer to its satisfying location.  
**PARTIAL:** Some mechanism-defining criteria carry self-referential belt labels; others do not.  
**FAIL:** No mechanism-defining criterion carries a self-referential belt label.

---

### C-27 — Spine-as-sole-suspenders declaration
The verification spine step header carries an explicit declaration that the spine is the consolidated suspenders layer for all `[C-NN: BELT]` labels in the prompt, of the form: `[C-25: BELT confirmed] — Consolidated suspenders for all [C-NN: BELT] labels in this prompt`. This declaration retires the VERIFICATION MANIFEST — once present, no separate VERIFICATION MANIFEST should appear. Spine-plus-manifest (both present) counts as a duplication failure.

**PASS:** Spine header carries explicit consolidated-suspenders declaration; no separate VERIFICATION MANIFEST present.  
**PARTIAL:** Spine present but consolidated-suspenders declaration absent, or spine and VERIFICATION MANIFEST both present (duplication).  
**FAIL:** No spine, or spine without declaration while VERIFICATION MANIFEST is retained.
```

**What was extracted and why:**

| Signal | New Criterion | Rationale |
|--------|--------------|-----------|
| Each new C-23/24/25 criterion carries its own `[C-NN: BELT]` label, proving itself | **C-26** Self-referential criterion enforcement | V-05 showed this is a distinct, verifiable property — a mechanism that doesn't apply to itself is weaker than one that does |
| V-05 declares the spine as the *sole* suspenders layer, eliminating VERIFICATION MANIFEST duplication | **C-27** Spine-as-sole-suspenders declaration | V-03 had both artifacts (duplication); V-05 resolved it with a single explicit declaration — the declaration is the distinguishing act |
