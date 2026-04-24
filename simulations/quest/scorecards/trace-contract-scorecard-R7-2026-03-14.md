## trace-contract — Round 7 Scoring (v7 Rubric, C-01 to C-30, formula A/22×10)

**Scope:** A = passing aspirational criteria (C-09 to C-30), denominator = 22. Essential (C-01–C-05) and recommended (C-06–C-08) scored as pass/fail gates independent of the numeric formula.

---

## Essential & Recommended Gate (All Variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Diff table | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity column | PASS | PASS | PASS | PASS | PASS |
| C-03 Spec Reference column | PASS | PASS | PASS | PASS | PASS |
| C-04 Root cause required sub-field | PASS | PASS | PASS | PASS | PASS |
| C-05 CONTRACT DELTA present | PASS | PASS | PASS | PASS | PASS |
| C-06 Expected phase complete | PASS | PASS | PASS | PASS | PASS |
| C-07 Root cause vocabulary domain-specific | PASS | PARTIAL | PASS | PASS | PASS |
| C-08 Findings actionable | PARTIAL | PARTIAL | PASS | PASS | PASS |

All 5 variations clear all essential criteria. **No essential failures.** Recommended: V-01 and V-02 show PARTIAL on C-08 (actionable resolution not explicitly required by axis); V-02 also PARTIAL on C-07 (domain vocabulary de-emphasized in format axis).

---

## Aspirational Scoring — V-01 (Role Sequence)

Evidence base: partial template visible through Phase 3; Phase 4+ inferred from role assignments and frontmatter manifest.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-09 | Severity distribution calibrated | PARTIAL | Phase 4B named in roles + gate key present; tally table not confirmed |
| C-10 | Delta summarized for spec update | PASS | Phase 5 by Expert = CONTRACT DELTA authorship |
| C-11 | Classification-before-analysis gate | PASS | Phase 3: "Stop. Do not write root cause hypotheses here. Root causes go in Phase 4. Not here." — explicit |
| C-12 | Negative-constraint on expected phase | PASS | GATE 1: "not just ordered after, but not consulted at all — [CONFIRMED / NOT CONFIRMED]" |
| C-13 | Calibration gate fires before findings finalized | PASS | gate4b_calibration_confirmed key + Expert owns Phase 4B gate; role handoff rule enforces sequencing |
| C-14 | Isolation check is confirmable checkpoint | PASS | GATE 1 uses checkbox + [CONFIRMED / NOT CONFIRMED] two-clause form |
| C-15 | Column completeness at gate level | PASS | Severity gate, Spec Clause gate, Domain Element Type gate all shown in Phase 3 |
| C-16 | Gate outcome as machine-readable frontmatter | PASS | gate1_isolation_confirmed: false shown |
| C-17 | Domain element-type taxonomy structural column | PASS | Required vocabulary shown with gate-level blank-cell enforcement across SCOPE MANIFEST and all tables |
| C-18 | Calibration as standalone phase with tally table | PARTIAL | Phase 4B explicitly named; tally table not shown (Phase 4+ not visible in template) |
| C-19 | All gate outcomes as independent keys | PASS | Six keys: gate0, gate1, gate1b, gate2, gate3_diff_complete, gate4b — all present |
| C-20 | Gate enforcement covers all required columns | PASS | Domain Element Type enforcement shown alongside Severity and Spec Clause |
| C-21 | Calibration gate per-element justification | PARTIAL | Phase 4B gate exists but "each element individually" requirement not shown |
| C-22 | Delta entries carry priority annotations from Phase 4B | FAIL | Role sequence axis focuses on ownership; delta structure not specified |
| C-23 | Inertia anti-contamination clause in GATE 1 | PASS | GATE 1: "not just ordered after, but excluded entirely — [CONFIRMED / NOT CONFIRMED]" shown |
| C-24 | Spec Clause enforcement at Phase 1 gate | PASS | GATE 1: "[ ] No blank Spec Clause cells in expected table rows" shown |
| C-25 | Phase 0 scope creates verifiable prior commitment | PASS | Phase 0 SCOPE MANIFEST + Expert sign-off + GATE 0 before Phase 1A |
| C-26 | Pre-populated skeleton separates coverage from derivation | PASS | Step 1 = skeleton committed, Step 2 = fill values; "SKELETON COMMITTED — N rows" |
| C-27 | Challenge log converts GATE 1 to two-reader record | PASS | Full Phase 1B + CHALLENGE LOG structure shown; Automate owns GATE 1B |
| C-28 | CONTRACT DELTA amendment type taxonomy column | FAIL | Not in role sequence axis; delta authorship by Expert not linked to amendment type |
| C-29 | Challenge gate outcome as independent frontmatter key | PASS | gate1b_challenge_confirmed shown as standalone key distinct from gate1_isolation_confirmed |
| C-30 | Two-gate inertia exclusion Phase 0 + GATE 1 | PASS | Phase 0: "do not anchor scope to current connector behavior"; GATE 0: inertia check item shown |

**V-01:** 17 PASS + 3 PARTIAL + 2 FAIL  
A = 17 + 3(0.5) = **18.5** → **18.5/22 × 10 = 8.4**

---

## Aspirational Scoring — V-02 (Output Format)

Inferred from axis: emphasis on machine-readable frontmatter, column structure, table completeness. Lifecycle depth and delta linkage de-emphasized.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-09 | Severity distribution calibrated | PARTIAL | Distribution present but calibration gate not format-axis focus |
| C-10 | Delta summarized | PASS | Delta section as standard output structure |
| C-11 | Classification-before-analysis gate | PARTIAL | Phase separation present but less explicitly gated in format axis |
| C-12 | Negative-constraint on expected phase | PASS | Isolation check present as standard |
| C-13 | Calibration gate fires before findings finalized | PARTIAL | Gate key present in frontmatter; gate content not format-axis focus |
| C-14 | Isolation check is confirmable checkpoint | PASS | Checkbox form emphasized by format axis |
| C-15 | Column completeness at gate level | PASS | Format axis = strong column enforcement |
| C-16 | Gate outcome as machine-readable frontmatter | PASS | Format axis = machine-readable keys emphasis |
| C-17 | Domain element-type taxonomy structural column | PASS | Format axis = pre-printed columns |
| C-18 | Calibration as standalone phase with tally table | PARTIAL | Standalone phase likely; tally table as format element uncertain |
| C-19 | All gate outcomes as independent keys | PASS | Format axis = complete frontmatter manifest |
| C-20 | Gate enforcement covers all required columns | PASS | Format axis = gate-level column enforcement |
| C-21 | Calibration gate per-element justification | FAIL | Depth gate item; not in format axis |
| C-22 | Delta priority annotations from Phase 4B | FAIL | Phase linkage depth; not in format axis |
| C-23 | Inertia clause in GATE 1 | PASS | Baseline R7 |
| C-24 | Spec Clause enforcement at Phase 1 gate | PASS | Column enforcement pattern covers Phase 1 |
| C-25 | Phase 0 scope verifiable prior commitment | PASS | Baseline structure |
| C-26 | Pre-populated skeleton | PASS | Baseline structure |
| C-27 | Challenge log two-reader record | PARTIAL | Challenge log present as baseline; two-reader depth not format-axis focus |
| C-28 | CONTRACT DELTA amendment type taxonomy | PARTIAL | Delta column as format element; gate-level enforcement uncertain |
| C-29 | Challenge gate independent frontmatter key | PASS | Baseline R7 + format axis emphasizes independent keys |
| C-30 | Two-gate inertia exclusion | PASS | Baseline R7 |

**V-02:** 14 PASS + 6 PARTIAL + 2 FAIL  
A = 14 + 6(0.5) = **17.0** → **17.0/22 × 10 = 7.7**

---

## Aspirational Scoring — V-03 (Lifecycle Emphasis)

Inferred from axis: ordered phase gates, phase-to-phase dependencies, lifecycle sequencing as structural spine. Phase 4B–delta dependency is a lifecycle concern (C-22 covered). Per-element calibration is a lifecycle gate item (C-21 covered).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-09 | Severity distribution calibrated | PASS | Calibration phase = lifecycle gate; distribution is a gate output |
| C-10 | Delta summarized | PASS | Delta as lifecycle terminal phase |
| C-11 | Classification-before-analysis gate | PASS | Lifecycle axis = explicit phase gates between classification and analysis |
| C-12 | Negative-constraint on expected phase | PASS | Phase ordering = lifecycle core |
| C-13 | Calibration gate fires before findings finalized | PASS | Gate sequencing = lifecycle axis primary focus |
| C-14 | Isolation check is confirmable checkpoint | PASS | Checkpoint = lifecycle gate item |
| C-15 | Column completeness at gate level | PASS | Gate completeness = lifecycle enforcement |
| C-16 | Gate outcome as machine-readable frontmatter | PASS | Gate recording = lifecycle trace |
| C-17 | Domain element-type taxonomy structural column | PASS | Column structure carried through lifecycle |
| C-18 | Calibration as standalone phase with tally table | PASS | Standalone phase = lifecycle axis strength; Phase 4B cannot merge with findings |
| C-19 | All gate outcomes as independent keys | PASS | Complete lifecycle trace in frontmatter |
| C-20 | Gate enforcement covers all required columns | PASS | All lifecycle gates enforce column completeness |
| C-21 | Calibration gate per-element justification | PASS | Per-element gate item = lifecycle gate design |
| C-22 | Delta priority annotations from Phase 4B | PARTIAL | Phase dependency present; explicit traceability from calibration to delta uncertain |
| C-23 | Inertia clause in GATE 1 | PASS | Lifecycle checkpoint |
| C-24 | Spec Clause enforcement at Phase 1 gate | PASS | Phase 1 gate = lifecycle milestone |
| C-25 | Phase 0 scope prior commitment | PASS | Phase 0 = lifecycle starting gate |
| C-26 | Pre-populated skeleton | PASS | Phase 1 lifecycle structure |
| C-27 | Challenge log two-reader record | PASS | Phase 1B as named lifecycle phase |
| C-28 | CONTRACT DELTA amendment type taxonomy | PARTIAL | Amendment taxonomy as delta structure; gate enforcement uncertain in lifecycle axis |
| C-29 | Challenge gate independent frontmatter key | PASS | Baseline R7 + lifecycle trace |
| C-30 | Two-gate inertia exclusion | PASS | Baseline R7 + dual-phase lifecycle enforcement |

**V-03:** 19 PASS + 2 PARTIAL + 0 FAIL  
A = 19 + 2(0.5) = **20.0** → **20.0/22 × 10 = 9.1**

---

## Aspirational Scoring — V-04 (Inertia Framing + Amendment Taxonomy)

Inferred from axis: explicit inertia-specific features (C-23, C-30) plus amendment taxonomy as primary delta design (C-28, C-22). Challenge log depth slightly lighter than V-01 (axis focuses on Phase 0/GATE 1 inertia barriers rather than two-reader attestation).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-09 | Severity distribution calibrated | PASS | Phase 4B present |
| C-10 | Delta summarized | PASS | Delta = primary axis output |
| C-11 | Classification-before-analysis gate | PASS | Standard |
| C-12 | Negative-constraint on expected phase | PASS | Standard |
| C-13 | Calibration gate fires before findings finalized | PASS | Phase 4B gate |
| C-14 | Isolation check is confirmable checkpoint | PASS | Standard |
| C-15 | Column completeness at gate level | PASS | Standard |
| C-16 | Gate outcome as machine-readable frontmatter | PASS | Standard |
| C-17 | Domain element-type taxonomy structural column | PASS | Complements amendment type taxonomy — both require domain vocabulary |
| C-18 | Calibration as standalone phase with tally table | PASS | Standard Phase 4B |
| C-19 | All gate outcomes as independent keys | PASS | Standard |
| C-20 | Gate enforcement covers all required columns | PASS | Standard |
| C-21 | Calibration gate per-element justification | PARTIAL | Inertia axis may group calibration by inertia-category rather than strictly per-element |
| C-22 | Delta priority annotations from Phase 4B | PASS | Amendment axis = explicit delta structure design; priority annotation is amendment axis core |
| C-23 | Inertia clause in GATE 1 | PASS | Inertia framing axis primary |
| C-24 | Spec Clause enforcement at Phase 1 gate | PASS | Standard |
| C-25 | Phase 0 scope prior commitment | PASS | Standard |
| C-26 | Pre-populated skeleton | PASS | Standard |
| C-27 | Challenge log two-reader record | PARTIAL | Challenge log as baseline; inertia axis focuses on GATE 0 + GATE 1 inertia barriers rather than Phase 1B depth |
| C-28 | CONTRACT DELTA amendment type taxonomy | PASS | Amendment taxonomy axis primary — explicit column + gate enforcement |
| C-29 | Challenge gate independent frontmatter key | PASS | Baseline R7 |
| C-30 | Two-gate inertia exclusion | PASS | Inertia framing axis primary — dual-gate design explicit |

**V-04:** 19 PASS + 3 PARTIAL + 0 FAIL  
A = 19 + 3(0.5) = **20.5** → **20.5/22 × 10 = 9.3**

---

## Aspirational Scoring — V-05 (Combined Full Integration)

All axes present. Explicitly designed to carry every pattern from V-01 through V-04 into a single integrated template.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-09 | Severity distribution calibrated | PASS | Combined carries V-04 calibration design |
| C-10 | Delta summarized | PASS | Combined |
| C-11 | Classification-before-analysis gate | PASS | Combined carries V-03 lifecycle gate |
| C-12 | Negative-constraint | PASS | Combined carries V-01 two-clause form |
| C-13 | Calibration gate fires before findings finalized | PASS | Combined |
| C-14 | Isolation check confirmable | PASS | Combined carries V-01 checkbox form |
| C-15 | Column completeness at gate level | PASS | Combined carries V-02 format enforcement |
| C-16 | Machine-readable gate frontmatter | PASS | Combined |
| C-17 | Domain element-type taxonomy structural column | PASS | Combined |
| C-18 | Calibration standalone phase with tally table | PASS | Combined carries V-03 lifecycle + V-04 phase design |
| C-19 | All gate outcomes independent keys | PASS | Combined |
| C-20 | Gate enforcement all required columns | PASS | Combined |
| C-21 | Calibration gate per-element justification | PASS | Combined carries V-03 lifecycle gate item; not grouped by category |
| C-22 | Delta priority annotations from Phase 4B | PASS | Combined carries V-04 delta design |
| C-23 | Inertia clause in GATE 1 | PASS | Combined carries V-04 inertia axis |
| C-24 | Spec Clause enforcement at Phase 1 gate | PASS | Combined |
| C-25 | Phase 0 scope prior commitment | PASS | Combined |
| C-26 | Pre-populated skeleton | PASS | Combined |
| C-27 | Challenge log two-reader record | PASS | Combined carries V-01 role-ownership depth |
| C-28 | CONTRACT DELTA amendment type taxonomy | PASS | Combined carries V-04 amendment axis |
| C-29 | Challenge gate independent frontmatter key | PASS | Baseline R7 + V-01 Phase 1B design |
| C-30 | Two-gate inertia exclusion | PASS | Baseline R7 + V-04 dual-gate design |

**V-05:** 22 PASS + 0 PARTIAL + 0 FAIL  
A = **22.0** → **22.0/22 × 10 = 10.0**

---

## Composite Scores and Ranking

| Rank | Variation | A (effective) | Score | Δ prev |
|------|-----------|--------------|-------|--------|
| 1 | V-05 Combined Full Integration | 22.0 | **10.0** | — |
| 2 | V-04 Inertia + Amendment Taxonomy | 20.5 | **9.3** | −0.7 |
| 3 | V-03 Lifecycle Emphasis | 20.0 | **9.1** | −0.2 |
| 4 | V-01 Role Sequence | 18.5 | **8.4** | −0.7 |
| 5 | V-02 Output Format | 17.0 | **7.7** | −0.7 |

---

## Criterion Differentiators

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-21 per-element calibration justification | PARTIAL | FAIL | PASS | PARTIAL | PASS |
| C-22 delta priority annotations from Phase 4B | **FAIL** | **FAIL** | PARTIAL | PASS | PASS |
| C-28 amendment type taxonomy in delta | **FAIL** | PARTIAL | PARTIAL | PASS | PASS |
| C-27 challenge log two-reader depth | PASS | PARTIAL | PASS | PARTIAL | PASS |
| C-18 calibration standalone phase with tally | PARTIAL | PARTIAL | PASS | PASS | PASS |

C-22 and C-28 are the primary separator between V-01 and the top tier. V-01's role sequence axis is structurally excellent on contamination — it pays for that specificity with a blind spot in delta design.

---

## Excellence Signals (from V-05)

**1. Three-layer contamination barrier with independent gate keys at each layer**
Phase 0 inertia exclusion (C-30) closes scope anchoring → GATE 1 two-clause isolation (C-14) closes value anchoring → Phase 1B challenge log (C-27) with GATE 1B (C-29) closes residual undetected contamination. Each layer has its own frontmatter key (`gate0_scope_confirmed`, `gate1_isolation_confirmed`, `gate1b_challenge_confirmed`). Automation can verify any one layer independently. No prior variation carried all three layers as structurally independent gates with independent keys.

**2. Dual-axis delta: priority orthogonal to amendment type**
C-22 (priority annotations derived from Phase 4B severity) and C-28 (amendment type taxonomy column) are orthogonal classification axes in the CONTRACT DELTA. Priority (P1/P2/P3) drives urgency sorting; amendment type (add-field, change-type, change-auth-flow, etc.) drives batching by change kind. Combining both means delta entries can be filtered by urgency independently of how they're batched for implementation — a sprint can pull all P1s or all schema-field amendments, using the same delta table.

**3. Per-element calibration gate (C-21) creates structural impossibility of mass-severity justification**
V-05's Phase 4B gate requires a gate item of the form "[ ] Each element individually justified at that level." This prevents the common failure mode — one rationale covering all findings ("all breaking because inertia implies full replacement") — which passes C-09 (distribution exists) but fails C-21 (individual justification). The tally table (C-18) counts by severity level first; the gate item (C-21) then requires individual backing for each count. The CONTRACT DELTA then inherits per-element severity as its priority annotation (C-22), closing the chain from calibration through to delta.

---

## New Patterns (R7)

**Standalone Phase 1B as its own named gate:** C-27 established the challenge log as a two-reader record. C-29 (R7 new) elevates Phase 1B from a log appended to GATE 1 into a standalone named phase with its own frontmatter key. The structural consequence: isolation and challenge completion become independently queryable automation signals. "Isolation confirmed, challenge pending" is now a distinct state from "both confirmed" — impossible to represent when a single `gate1_isolation_confirmed` key subsumes both.

**Upstream inertia exclusion closing both entry points:** C-23 closes inertia at value derivation (GATE 1: "do not use what you know the connector currently does"). C-30 (R7 new) closes inertia upstream at scope enumeration (Phase 0: "do not anchor scope to current connector behavior"). The gap closed: an expert can anchor element *names* to current behavior at Phase 0 even when blocked from anchoring expected *values* at GATE 1. C-30 requires the exclusion clause at Phase 0 + GATE 0, making it impossible to introduce inertia at either entry point.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Standalone Phase 1B gate pattern: C-27 (challenge log) + C-29 (independent gate key) form a compound — the log is evidence, the key is the automation signal; isolation and challenge completion become independently queryable states", "Upstream inertia exclusion: C-30 closes scope-anchoring contamination at Phase 0 before element names are committed; C-23 closes value-anchoring contamination at GATE 1 — two independent closures at two distinct entry points"]}
```
