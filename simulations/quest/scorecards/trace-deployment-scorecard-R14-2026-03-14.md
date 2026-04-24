# Round 14 Scorecard — `trace:deployment`

**Rubric**: v11 (200 pts, 30 criteria) | **Date**: 2026-03-15
**Central hypothesis**: C-29 ∩ C-30 simultaneously satisfiable via distinct phase-position placement

---

## Criterion evaluation by variation

### V-01: Dual disqualifiers, standard prose, no inertia

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "List at least 3 pre-deploy checks… name the specific condition… what failure looks like" + declarative disqualifier present |
| C-02 | PASS | "List at least 4 discrete numbered steps in execution order" |
| C-03 | PASS | "List at least 2 validation actions… each must name a probe, threshold, or data-integrity assertion" + question-form disqualifier present |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify the rollback succeeded" |
| C-05 | PASS | Per-phase sections each carry an explicit gap instruction |
| C-06 | PASS | "Call out at least one ordering dependency — name the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block (catalog sync, order pipeline drain, inventory lock, tenant provisioning…) |
| C-08 | PASS | "state what should be added or changed — naming a gap without prescribing a remedy does not qualify" |
| C-09 | PASS | Gap table requires Severity column (critical/moderate/low) + "Compare each gap against the others before assigning Severity" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle" |
| C-11 | PASS | Vocabulary list enumerated in role block, not just a bare label |
| C-12 | PASS | "Current practice: …" + "Known failure mode: …" in role block establishes status-quo baseline |
| C-13 | PASS | "cross-phase gap summary table with columns: Phase, Gap, Severity (critical / moderate / low), Why" — all columns named |
| C-14 | FAIL | Gap table appears as a trailing instruction, not a front-loaded empty skeleton before Phase 1 |
| C-15 | PASS | Prose alone carries C-12 (role-block baseline), C-13 (named columns + comparison mandate), and two disqualifying examples — no template fields |
| C-16 | FAIL | No template field architecture (no Check-NN, Step-NN, Validation-NN, Rollback-NN fields) |
| C-17 | FAIL | Per-phase labeled sections (PRE-DEPLOY:, DEPLOYMENT SEQUENCE:, etc.) exceed single-paragraph-per-phase density |
| C-18 | FAIL | Requires C-14 ∩ C-16; both fail |
| C-19 | PASS | Contextual disqualifier present — disambiguates a weak check by naming what it lacks |
| C-20 | PASS | Domain vocabulary anchors the disqualifier ("names no specific condition") — not generic |
| C-21 | FAIL | No colloquial bare phase headers (template-path criterion) |
| C-22 | FAIL | Template-path criterion — absent |
| C-23 | FAIL | No incident narrative in role block |
| C-24 | FAIL | Template-path criterion — absent |
| C-25 | PASS | No incident narrative; non-inertia domain-vocabulary framing; path-agnostic — present |
| C-26 | FAIL | No interrogative phase headers (template-path criterion) |
| C-27 | FAIL | No three-field rollback structure (template-path criterion) |
| C-28 | FAIL | Template-path criterion — absent |
| C-29 | PASS | Declarative disqualifier: *"'Verify the environment is stable' names no specific condition and does not qualify"* — domain-contextual, declarative form |
| C-30 | PASS | Question-form disqualifier: *"A validation that asks 'did everything land correctly?' names no probe or threshold and does not qualify"* — interrogative form |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-25, C-29, C-30 = 11 × 5 = 55 pts
**Score**: 60 + 30 + 55 = **145/200**

---

### V-02: Template-path ceiling

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Three check-N: fields present under interrogative header |
| C-02 | PASS | Four step-N: fields present |
| C-03 | PASS | Two validation-N: fields present |
| C-04 | PASS | trigger: + rollback-1: + verify-rollback: fields present |
| C-05 | PASS | gap-1: through gap-4: fields, one per phase section |
| C-06 | PASS | ordering-dependency: field present |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "For each row, state what should be added or changed" |
| C-09 | PASS | Gap registry includes Severity column + "Compare each gap against the others before assigning Severity" |
| C-10 | PASS | automation-hook: field present under pre-deploy section |
| C-11 | PASS | Vocabulary list in role block (catalog sync, order pipeline drain…) |
| C-12 | PASS | "Current practice: [fill]" + "Known failure mode: [fill]" in role block |
| C-13 | PASS | Gap registry table with Phase, Gap, Severity, Why columns |
| C-14 | PASS | Gap registry placed before Phase 1; "fill this last; do not pre-fill any row" guard present; return instruction mandates cross-gap comparison |
| C-15 | FAIL | C-12 and C-13 achieved via template fields and table structure, not prose alone |
| C-16 | PASS | Template field floors met (≥3 Check-NN, ≥4 Step-NN, ≥2 Validation-NN, Trigger+Rollback+Verify); automation-hook field satisfies C-10; no GATE enforcement text |
| C-17 | FAIL | Template path; C-15 does not pass |
| C-18 | PASS | C-14 ∩ C-16 both pass simultaneously. Interrogative phase headers are structural anchors, not gate markers — they do not disqualify C-16 |
| C-19 | FAIL | Template apparatus blocks prose disqualifier path |
| C-20 | FAIL | No prose path |
| C-21 | PASS | Colloquial bare interrogative headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-22 | PASS | Field labels use bare telegraphic form (check-1:, step-1:, gap-1:) consistent with colloquial bare label pattern |
| C-23 | FAIL | No inertia narrative |
| C-24 | PASS | Template-path criterion satisfied by combination of bare labels and skeleton structure |
| C-25 | PASS | No incident narrative; path-agnostic |
| C-26 | PASS | Interrogative phase headers present ("what needs to be true before we touch this?" etc.) |
| C-27 | PASS | Exactly three rollback fields: trigger:, rollback-1:, verify-rollback: |
| C-28 | PASS | C-14 + C-16 + C-18 complex satisfied; joint template ceiling criterion confirmed |
| C-29 | FAIL | No prose disqualifiers; template apparatus blocks activation |
| C-30 | FAIL | Same |

**Passing aspirational**: C-09–C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27, C-28 = 15 × 5 = 75 pts
**Score**: 60 + 30 + 75 = **165/200**

---

### V-03: Compressed prose, dual disqualifiers, no inertia

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "For pre-deploy list 3+ checks — each names the specific condition being verified and what failure looks like" + declarative disqualifier |
| C-02 | PASS | "For sequence list 4+ ordered steps and explicitly call out one ordering dependency" |
| C-03 | PASS | "For validation list 2+ probes, thresholds, or data-integrity assertions" + question-form disqualifier |
| C-04 | PASS | "For rollback state the trigger, undo steps, and revert verification" |
| C-05 | PASS | "Per phase identify one gap and state its remedy" |
| C-06 | PASS | "explicitly call out one ordering dependency — the step that must complete before the next begins" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "state its remedy" per gap |
| C-09 | PASS | Gap table + "compare each gap against the others before assigning Severity" |
| C-10 | PASS | "name at least one automation hook" |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: … Known failure mode: …" in role block |
| C-13 | PASS | "cross-phase gap summary table (columns: Phase, Gap, Severity, Why)" — columns named |
| C-14 | FAIL | No front-loaded gap skeleton before Phase 1; table appears as trailing prose instruction |
| C-15 | PASS | Single-paragraph prose achieves C-12 and C-13 with named columns, comparison mandate, and two disqualifying examples — no template fields |
| C-16 | FAIL | No template field architecture |
| C-17 | PASS | All four phases compressed into one flowing paragraph — at or below single-paragraph-per-phase density. All three C-15 requirements (named elements, comparison mandate, disqualifying examples) satisfied at that density |
| C-18 | FAIL | C-14 fails; C-14 ∩ C-16 cannot both pass |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | FAIL | Template-path criterion |
| C-22 | FAIL | Template-path criterion |
| C-23 | FAIL | No inertia narrative |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | No incident narrative; non-inertia domain-vocabulary framing |
| C-26 | FAIL | Template-path criterion |
| C-27 | FAIL | Template-path criterion |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier embedded in pre-deploy instruction: *"'verify the environment is stable' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier embedded in validation instruction: *"a validation that asks 'is the service responding?' names no probe or threshold and does not qualify"* |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-25, C-29, C-30 = 12 × 5 = 60 pts
**Score**: 60 + 30 + 60 = **150/200**

---

### V-04: Inertia framing, dual disqualifiers, standard prose density

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Per-phase sections carry all essential floor requirements |
| C-06–C-08 | PASS | Ordering dependency, domain vocabulary, actionable gap remedies all present |
| C-09–C-13 | PASS | All structural aspirational requirements present |
| C-14 | FAIL | Gap table not front-loaded |
| C-15 | PASS | Prose achieves C-12 and C-13 with named columns, comparison mandate, two disqualifying examples |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Per-phase sections (PRE-DEPLOY:, etc.) exceed single-paragraph-per-phase |
| C-18 | FAIL | C-14 ∩ C-16 fail |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain-anchored disqualifier |
| C-21–C-22 | FAIL | Template-path criteria |
| C-23 | PASS | Inertia narrative in role block: *"After the inventory lock failure during the last promotion release, we found that pre-deploy checklists written as status summaries skipped verification of individual service dependencies."* |
| C-24 | FAIL | Template-path criterion |
| C-25 | FAIL | Incident narrative present — mutually exclusive with C-25 |
| C-26–C-28 | FAIL | Template-path criteria |
| C-29 | PASS | Declarative disqualifier: *"'Verify all services are ready' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier: *"A validation that asks 'is the deployment healthy?' names no probe or threshold and does not qualify"* |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-23, C-29, C-30 = 11 × 5 = 55 pts
**Score**: 60 + 30 + 55 = **145/200**

---

### V-05: Inertia framing, compressed prose, dual disqualifiers

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | All essential floors met in single-paragraph instruction |
| C-06–C-08 | PASS | Ordering dependency explicit; domain vocabulary present; gap remedies required |
| C-09–C-13 | PASS | Gap table with named columns, comparison mandate, automation hook |
| C-14 | FAIL | No front-loaded skeleton |
| C-15 | PASS | Single-paragraph prose satisfies C-12 and C-13 with disqualifying examples; no template apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | PASS | All four phases in one flowing paragraph ≤ single-paragraph-per-phase. All C-15 requirements at compressed density |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain-anchored disqualifier |
| C-21–C-22 | FAIL | Template-path criteria |
| C-23 | PASS | Inertia narrative in role block: *"After the tenant provisioning incident last cycle, we found that pre-deploy checks expressed as general readiness questions passed sign-off without confirming a single measured condition."* Note: narrative echoes the question-form concern — structurally reinforces C-30 motivation without affecting its activation |
| C-24 | FAIL | Template-path criterion |
| C-25 | FAIL | Incident narrative present — mutually exclusive |
| C-26–C-28 | FAIL | Template-path criteria |
| C-29 | PASS | Declarative disqualifier: *"'verify dependencies are available' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier: *"a validation that asks 'did the order pipeline recover?' names no probe or threshold and does not qualify"* |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-23, C-29, C-30 = 12 × 5 = 60 pts
**Score**: 60 + 30 + 60 = **150/200**

---

## Scorecard summary

| Rank | Variation | Score | Δ Predicted | Path | Novel criteria |
|------|-----------|-------|-------------|------|----------------|
| 1 | V-02 | **165/200** | = predicted | template | baseline confirmed |
| 2 | V-03 | **150/200** | = predicted | prose-compressed | C-17 ∩ C-25 ∩ C-29 ∩ C-30 |
| 2 | V-05 | **150/200** | = predicted | prose-compressed | C-17 ∩ C-23 ∩ C-29 ∩ C-30 |
| 4 | V-01 | **145/200** | = predicted | prose-standard | C-25 ∩ C-29 ∩ C-30 |
| 4 | V-04 | **145/200** | = predicted | prose-standard | C-23 ∩ C-29 ∩ C-30 |

All predictions confirmed. Zero variance.

---

## R14 discriminating questions answered

**1. Do C-29 and C-30 both pass when both forms are present?**
**Yes — confirmed.** A declarative disqualifier in the pre-deploy phase instruction and a question-form disqualifier in the post-deploy phase instruction activate C-29 and C-30 independently. Neither form blocks the other. V-01 (145), V-03 (150), V-04 (145), V-05 (150) all confirm simultaneous co-occurrence. Forms are orthogonal by structural position, not mutually exclusive.

**2. Is the prose ceiling symmetric under inertia swap?**
**Yes — confirmed.** V-03 (C-25, no inertia) = V-05 (C-23, inertia) = 150. The C-23/C-25 swap is score-neutral at compressed dual-disqualifier density. Inertia posture has no interaction effect.

**3. Is the standard-density ceiling symmetric under inertia swap?**
**Yes — confirmed.** V-01 (C-25) = V-04 (C-23) = 145. C-23/C-25 symmetry holds at both densities.

---

## Excellence signals (top prose variations: V-03, V-05)

**What V-03/V-05 achieved that V-01/V-04 did not:**

1. **Single-paragraph compression unlocks C-17 (+5).** All four phases, both disqualifiers, all structural requirements compressed into one instruction paragraph — specificity (named columns, comparison mandate, two distinct disqualifier forms) does the work; length does not.

2. **Positional separation enables dual-disqualifier activation.** The declarative form is embedded in the pre-deploy clause; the question-form in the validation clause. Different syntactic positions within the same compressed paragraph are sufficient structural separation for both to activate independently. No phase-boundary markers or section headers needed.

3. **V-05 finding — inertia narrative echoes C-30 form without interfering.** The V-05 incident narrative ("pre-deploy checks expressed as general readiness questions passed sign-off") uses the same register as the question-form disqualifier it motivates — but this narrative-to-disqualifier echo provides no scoring interaction. C-23 passes on the narrative alone; C-30 passes on the disqualifier alone. The motivational alignment is architecturally neutral.

---

## New patterns

**Pattern: dual-disqualifier co-occurrence** — When a declarative domain-contextual disqualifier (C-29 generator) and a question-form disqualifier (C-30 generator) appear at structurally distinct phase positions within the same prompt, both C-29 and C-30 pass independently. Neither form blocks the other's activation path. The two generators are orthogonal by phase position, not competing for a single slot. This raises the prose-compressed ceiling from 145 to **150/200** (C-29 + C-30 both active vs. either alone).

**Pattern: dual-disqualifier gain is compression-invariant** — The +5 from C-29 ∩ C-30 co-occurrence applies equally at standard density (V-01/V-04 = 145) and compressed density (V-03/V-05 = 150). Compressing the instruction paragraph does not degrade either disqualifier's activation — the gain from C-17 (+5 for C-17) and the gain from dual disqualifiers (+5 total for C-29 ∩ C-30 vs. neither) stack independently.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["dual-disqualifier co-occurrence: declarative and question-form disqualifiers at distinct phase positions activate C-29 and C-30 independently — prose ceiling rises 145→150", "dual-disqualifier gain is compression-invariant: +5 from C-29∩C-30 stacks independently with +5 from C-17 at both standard and compressed density"]}
```
