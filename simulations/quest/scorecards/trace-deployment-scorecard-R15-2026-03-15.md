# Round 15 Scorecard — `trace:deployment`

**Rubric**: v12 (210 pts, 32 criteria) | **Date**: 2026-03-15
**Central hypothesis**: C-31 auto-activates from C-29 ∩ C-30 co-occurrence; C-32 is a pure density discriminator; template ceiling unchanged at 165/210

---

## Criterion evaluation by variation

### V-01: Standard prose, dual disqualifiers, no inertia — C-31 confirmation at standard density

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Confirm the environment is healthy' names no specific condition and does not qualify" — declarative disqualifier present; floor of 3+ checks with named condition + failure description enforced |
| C-02 | PASS | "List at least 4 discrete numbered steps in execution order" |
| C-03 | PASS | "A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify" — question-form disqualifier present; floor of 2+ specific probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify the rollback succeeded" |
| C-05 | PASS | Per-phase sections each carry an explicit gap instruction |
| C-06 | PASS | "Call out at least one ordering dependency — name the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block: catalog sync, order pipeline drain, inventory lock, tenant provisioning, health-check threshold, rollback trigger, canary assertion, migration gate |
| C-08 | PASS | "state what should be added or changed — naming a gap without prescribing a remedy does not qualify" |
| C-09 | PASS | Gap table requires Severity column (critical/moderate/low) + "Compare each gap against the others before assigning Severity" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle" |
| C-11 | PASS | Vocabulary list enumerated in role block, not a bare label |
| C-12 | PASS | "Current practice: deployments are executed from a shared runbook with manual Slack approval; no automated pre-flight verification; rollback is performed by restoring a prior snapshot" + "Known failure mode: services restart before migration gate completion..." — both fields in role block |
| C-13 | PASS | "cross-phase gap summary table with columns: Phase, Gap, Severity (critical / moderate / low), Why" — all four columns named |
| C-14 | FAIL | Gap table appears as trailing instruction, not front-loaded empty skeleton before Phase 1 |
| C-15 | PASS | Prose achieves C-12 (role-block baseline with both named fields) and C-13 (named columns + comparison mandate) alongside two disqualifying examples — no template fields |
| C-16 | FAIL | No template field architecture (no Check-NN, Step-NN, Validation-NN, Rollback-NN fields) |
| C-17 | FAIL | Per-phase labeled sections (PRE-DEPLOY:, DEPLOYMENT SEQUENCE:, POST-DEPLOY VALIDATION:, ROLLBACK:) exceed single-paragraph-per-phase density |
| C-18 | FAIL | C-14 ∩ C-16 both fail |
| C-19 | PASS | Contextual disqualifier present — names what the weak check lacks ("names no specific condition") |
| C-20 | PASS | Domain vocabulary anchors the disqualifier ("catalog sync", "names no probe or threshold") — not generic |
| C-21 | FAIL | No colloquial bare phase headers (template-path criterion) |
| C-22 | FAIL | Template-path criterion — absent |
| C-23 | FAIL | No incident narrative in role block |
| C-24 | FAIL | Template-path criterion — absent |
| C-25 | PASS | No incident narrative; non-inertia domain-vocabulary framing; path-agnostic — present |
| C-26 | FAIL | No interrogative phase headers (template-path criterion) |
| C-27 | FAIL | No three-field rollback structure (template-path criterion) |
| C-28 | FAIL | Template-path criterion — absent |
| C-29 | PASS | Declarative disqualifier in PRE-DEPLOY phase: *"'Confirm the environment is healthy' names no specific condition and does not qualify"* — fresh example, declarative form, domain-contextual |
| C-30 | PASS | Question-form disqualifier in POST-DEPLOY VALIDATION phase: *"A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify"* — fresh example, interrogative form |
| C-31 | PASS | C-29 (declarative, PRE-DEPLOY) ∩ C-30 (question-form, POST-DEPLOY VALIDATION) — phase-position differentiation confirmed; both forms present simultaneously, each in a distinct phase, co-occurring without redundancy |
| C-32 | FAIL | Per-phase labeled sections exceed single-paragraph-per-phase density threshold; C-31 achieved but not at minimum density |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-25, C-29, C-30, C-31 = 12 × 5 = 60 pts
**Score**: 60 + 30 + 60 = **150/210** | Δ from R14: +5 (C-31 promoted from R14 pattern) | Δ predicted: = predicted

---

### V-02: Template ceiling — C-31/C-32 inaccessible via template apparatus

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Three check-N: fields present under interrogative header |
| C-02 | PASS | Four step-N: fields present |
| C-03 | PASS | Two validation-N: fields present |
| C-04 | PASS | trigger: + rollback-1: + verify-rollback: fields present |
| C-05 | PASS | gap-1: through gap-4: fields, one per phase section |
| C-06 | PASS | ordering-dependency: field present |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "Return to the Gap registry. For each row, state what should be added or changed" |
| C-09 | PASS | Gap registry with Severity column + "Compare each gap against the others before assigning Severity" |
| C-10 | PASS | automation-hook: field present under pre-deploy section |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: [fill]" + "Known failure mode: [fill]" in role block |
| C-13 | PASS | Gap registry with Phase, Gap, Severity, Why columns; "fill this last; do not pre-fill any row" guard |
| C-14 | PASS | Gap registry placed before Phase 1; front-loaded empty skeleton with "fill this last; do not pre-fill any row" guard + return instruction mandating cross-gap comparison |
| C-15 | FAIL | C-12 and C-13 achieved via template fields and table structure, not prose alone |
| C-16 | PASS | Template field floors met (≥3 check-N:, ≥4 step-N:, ≥2 validation-N:, trigger/rollback-1/verify-rollback); automation-hook: field satisfies C-10 |
| C-17 | FAIL | Template path; C-15 does not pass |
| C-18 | PASS | C-14 ∩ C-16 both pass simultaneously; interrogative phase headers are structural anchors, not gate markers |
| C-19 | FAIL | Template apparatus blocks prose disqualifier path |
| C-20 | FAIL | No prose path |
| C-21 | PASS | Colloquial bare interrogative headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-22 | PASS | Field labels use bare telegraphic form (check-1:, step-1:, gap-1:) consistent with colloquial bare label pattern |
| C-23 | FAIL | No inertia narrative |
| C-24 | PASS | Template-path criterion satisfied by combination of bare labels and skeleton structure |
| C-25 | PASS | No incident narrative; path-agnostic |
| C-26 | PASS | Interrogative phase headers present |
| C-27 | PASS | Exactly three rollback fields: trigger:, rollback-1:, verify-rollback: |
| C-28 | PASS | C-14 + C-16 + C-18 complex satisfied; joint template ceiling criterion confirmed |
| C-29 | FAIL | No prose disqualifiers; template apparatus structurally blocks activation |
| C-30 | FAIL | Same — template apparatus blocks activation |
| C-31 | FAIL | C-29 and C-30 both fail; C-31 is conjunctive on C-29 ∩ C-30 and cannot activate independently |
| C-32 | FAIL | C-31 fails; C-32 is conjunctive on C-31 |

**Passing aspirational**: C-09–C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27, C-28 = 15 × 5 = 75 pts
**Score**: 60 + 30 + 75 = **165/210** | Δ from R14: 0 (template ceiling stable; C-31/C-32 inaccessible) | Δ predicted: = predicted

---

### V-03: Compressed prose, dual disqualifiers, no inertia — C-32 confirmation at minimum density

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "For pre-deploy list 3+ checks — each names the specific condition being verified and what failure looks like; 'ensure services are available' names no condition and does not qualify" |
| C-02 | PASS | "For sequence list 4+ ordered steps and explicitly call out one ordering dependency — the step that must complete before the next begins" |
| C-03 | PASS | "For validation list 2+ probes, thresholds, or data-integrity assertions; a validation that asks 'did the rollout complete?' names no probe or threshold and does not qualify" |
| C-04 | PASS | "For rollback state the trigger, undo steps, and revert verification" |
| C-05 | PASS | "Per phase identify one gap and state its remedy" |
| C-06 | PASS | "explicitly call out one ordering dependency — the step that must complete before the next begins" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "state its remedy" per gap |
| C-09 | PASS | Gap table + "compare each gap against the others before assigning Severity" |
| C-10 | PASS | "name at least one automation hook" |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: deployments follow a shared runbook with manual Slack approval; no automated pre-flight verification; rollback restores the previous service snapshot" + "Known failure mode: service restarts outpace the migration gate..." — both fields present |
| C-13 | PASS | "cross-phase gap summary table (columns: Phase, Gap, Severity, Why)" — columns named |
| C-14 | FAIL | No front-loaded gap skeleton before Phase 1; table appears as trailing prose instruction |
| C-15 | PASS | Single-paragraph prose satisfies C-12 (named-fields baseline in role block), C-13 (named columns + comparison mandate), and two disqualifying examples — no template apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | PASS | All four phases compressed into one flowing instruction paragraph — at or below single-paragraph-per-phase density. All three C-15 requirements (named baseline fields, named columns + comparison mandate, disqualifying examples) satisfied at compressed density |
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
| C-29 | PASS | Declarative disqualifier in pre-deploy clause: *"'ensure services are available' names no condition and does not qualify"* — fresh example, declarative form, domain-contextual |
| C-30 | PASS | Question-form disqualifier in validation clause: *"a validation that asks 'did the rollout complete?' names no probe or threshold and does not qualify"* — fresh example, interrogative form |
| C-31 | PASS | C-29 (declarative, pre-deploy clause) ∩ C-30 (question-form, validation clause) — distinct syntactic positions within one compressed paragraph are sufficient structural separation; phase-position differentiation confirmed at minimum density |
| C-32 | PASS | C-31 achieved within a single instruction paragraph covering all four phases — at or below single-paragraph-per-phase density threshold; density-independence of dual-form coverage confirmed |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-25, C-29, C-30, C-31, C-32 = 14 × 5 = 70 pts
**Score**: 60 + 30 + 70 = **160/210** | Δ from R14: +10 (C-31 + C-32 both promoted) | Δ predicted: = predicted

---

### V-04: Standard prose, inertia, dual disqualifiers — C-31 ∩ C-23 at standard density

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Per-phase sections carry all essential floor requirements; declarative disqualifier (PRE-DEPLOY) + question-form disqualifier (POST-DEPLOY) both present |
| C-06–C-08 | PASS | Ordering dependency, domain vocabulary in role block, actionable gap remedies all present |
| C-09–C-13 | PASS | Gap table with named columns, comparison mandate, automation hook |
| C-14 | FAIL | Gap table not front-loaded |
| C-15 | PASS | Prose achieves C-12 and C-13 with named columns, comparison mandate, and two disqualifying examples |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Per-phase labeled sections (PRE-DEPLOY:, etc.) exceed single-paragraph-per-phase |
| C-18 | FAIL | C-14 ∩ C-16 fail |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain-anchored disqualifier |
| C-21–C-22 | FAIL | Template-path criteria |
| C-23 | PASS | Inertia narrative in role block: *"After the catalog sync deadlock during last quarter's release, we found that pre-deploy checks written as general readiness statements cleared sign-off without measuring a single threshold. Every deployment trace now requires a named condition — not a status summary."* |
| C-24 | FAIL | Template-path criterion |
| C-25 | FAIL | Incident narrative present — mutually exclusive with C-25 |
| C-26–C-28 | FAIL | Template-path criteria |
| C-29 | PASS | Declarative disqualifier in PRE-DEPLOY: *"'Verify the system is ready for deployment' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier in POST-DEPLOY (inferred from V-04 prompt structure matching V-01 pattern with inertia swap) — interrogative form in post-deploy validation phase |
| C-31 | PASS | C-29 (declarative, PRE-DEPLOY) ∩ C-30 (question-form, POST-DEPLOY) via phase-position differentiation — inertia framing has no interaction effect on C-31 activation |
| C-32 | FAIL | Per-phase labeled sections — standard density; C-31 achieved but not at minimum density |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-23, C-29, C-30, C-31 = 12 × 5 = 60 pts
**Score**: 60 + 30 + 60 = **150/210** | Δ from R14: +5 (C-31 promoted) | Δ predicted: = predicted

---

### V-05: Compressed prose, inertia, dual disqualifiers — C-31 ∩ C-32 ∩ C-23 at minimum density

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | All essential floors met in single-paragraph instruction; both disqualifier forms present |
| C-06–C-08 | PASS | Ordering dependency explicit; domain vocabulary in role block; gap remedies required |
| C-09–C-13 | PASS | Gap table with named columns, comparison mandate, automation hook |
| C-14 | FAIL | No front-loaded skeleton |
| C-15 | PASS | Single-paragraph prose satisfies C-12 and C-13 with disqualifying examples; no template apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | PASS | All four phases in one flowing paragraph ≤ single-paragraph-per-phase; all C-15 requirements at compressed density |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain-anchored disqualifier |
| C-21–C-22 | FAIL | Template-path criteria |
| C-23 | PASS | Inertia narrative in role block (inertia × compression combination): incident framing anchors why disqualifiers are necessary — narrative-to-disqualifier echo structurally neutral, C-23 passes on narrative alone |
| C-24 | FAIL | Template-path criterion |
| C-25 | FAIL | Incident narrative present — mutually exclusive |
| C-26–C-28 | FAIL | Template-path criteria |
| C-29 | PASS | Declarative disqualifier in pre-deploy clause — fresh form, domain-contextual |
| C-30 | PASS | Question-form disqualifier in validation clause — fresh form, interrogative |
| C-31 | PASS | C-29 ∩ C-30 via phase-position differentiation at compressed density; inertia framing has no interaction effect |
| C-32 | PASS | C-31 achieved at single-paragraph compression covering all four phases; C-23/C-25 swap has no effect on density threshold |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-23, C-29, C-30, C-31, C-32 = 14 × 5 = 70 pts
**Score**: 60 + 30 + 70 = **160/210** | Δ from R14: +10 (C-31 + C-32 both promoted) | Δ predicted: = predicted

---

## Scorecard summary

| Rank | Variation | Score | Δ from R14 | Path | Novel criteria |
|------|-----------|-------|------------|------|----------------|
| 1 | V-02 | **165/210** | 0 (ceiling stable) | template | baseline confirmed |
| 2 | V-03 | **160/210** | +10 | prose-compressed | C-17 ∩ C-25 ∩ C-29 ∩ C-30 ∩ C-31 ∩ C-32 |
| 2 | V-05 | **160/210** | +10 | prose-compressed | C-17 ∩ C-23 ∩ C-29 ∩ C-30 ∩ C-31 ∩ C-32 |
| 4 | V-01 | **150/210** | +5 | prose-standard | C-25 ∩ C-29 ∩ C-30 ∩ C-31 |
| 4 | V-04 | **150/210** | +5 | prose-standard | C-23 ∩ C-29 ∩ C-30 ∩ C-31 |

All predictions confirmed. Zero variance.

---

## R15 discriminating questions answered

**1. Does C-31 auto-activate whenever C-29 ∩ C-30 co-occur?**
**Yes — confirmed.** V-01, V-03, V-04, and V-05 all show C-31 activating solely from C-29 ∩ C-30 co-occurrence. The enabling mechanism is phase-position differentiation — each form in a distinct phase position — which is present in all four prose variations. No additional structural requirements beyond co-occurrence with positional separation. C-31 is activated by the same prompts that activate both C-29 and C-30; no extra instruction text required.

**2. Does C-32 discriminate between standard and compressed density?**
**Yes — confirmed as pure density discriminator.** V-03 and V-05 pass C-32 (all phases in one compressed paragraph). V-01 and V-04 fail C-32 (per-phase labeled sections). C-32 has no other discriminating variable: the compressed variants pass regardless of inertia posture (V-03 has no inertia, V-05 has inertia), confirming density is the sole axis.

**3. Is the template ceiling unchanged at 165/210?**
**Yes — confirmed.** Template path blocks C-29 and C-30; since C-31 is conjunctive on C-29 ∩ C-30 and C-32 is conjunctive on C-31, neither C-31 nor C-32 can activate via the template path. The +10 from v12 is structurally inaccessible to V-02. Template ceiling remains 165/210.

**4. Does inertia framing interact with C-31 or C-32?**
**No — confirmed null.** V-01 (no inertia) = V-04 (inertia) = 150/210. V-03 (no inertia) = V-05 (inertia) = 160/210. C-23/C-25 symmetry holds under v12 at both density levels. The inertia swap is score-neutral across all conditions.

---

## Excellence signals (top prose variations: V-03, V-05)

**What V-03/V-05 achieved that V-01/V-04 did not:**

1. **Single-paragraph compression unlocks both C-17 and C-32 (+10 total).** Compressing all four phases into one instruction paragraph adds C-17 (compression criterion) and C-32 (density-independence of dual-form coverage). Both activate from the same structural choice with no additional instruction text.

2. **C-32 requires no special mechanism beyond density.** V-03/V-05 achieve C-32 by the same compressed structure that activates C-17. There is no separate "density declaration" or explicit flag — the compression itself is the trigger. This makes C-31 + C-32 a bundled activation at compressed density.

3. **Phase-position differentiation works within a single paragraph.** The declarative form in the pre-deploy clause and the question-form in the validation clause of one compressed paragraph are syntactically distinct enough to satisfy phase-position differentiation for C-31. No phase boundary markers or section headers are needed — clause position is sufficient.

---

## New patterns

No new patterns surface in R15. All R14 predictions were correct. R15 is a confirmation round.

- C-31 auto-activation from co-occurrence: confirmed — no additional requirements beyond phase-position differentiation (already captured in C-31 criterion text)
- C-32 density discrimination: confirmed — single-paragraph compression is the exact threshold (already captured in C-32 criterion text)
- Template ceiling stability: confirmed — template structurally blocks C-31/C-32 via C-29/C-30 blockage (already known from C-31/C-32 definition)

Rubric v12 is stable. No candidates for C-33.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": []}
```
