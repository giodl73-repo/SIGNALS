# Round 16 Scorecard — `trace:deployment`

**Rubric**: v12 (210 pts, 32 criteria) | **Date**: 2026-03-15
**Central questions**: Can C-14 activate on prose path? Are C-21/C-26 surface-form or template-exclusive? Is C-27 template-exclusive?
**R15 prose ceiling entering R16**: 160/210 (V-03/V-05) | **Template ceiling**: 165/210 (V-02)

---

## Criterion evaluation by variation

### V-01: Front-loaded gap table in prose — C-14 probe at standard density

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Confirm the environment is healthy' names no specific condition and does not qualify" — declarative disqualifier; 3+ checks with named condition + failure enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency explicitly" |
| C-03 | PASS | "A validation that asks 'did everything land correctly?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "Fill one row per phase" in return-to-gap-table instruction; one gap per phase enforced |
| C-06 | PASS | "Call out at least one ordering dependency explicitly — the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block: catalog sync, inventory lock, order pipeline drain, tenant provisioning, feature flag promotion, schema migration gate, canary validation, service mesh health probe, rollback trigger, deployment gate |
| C-08 | PASS | "state what should be added or changed — naming a gap without prescribing a remedy does not qualify" |
| C-09 | PASS | Gap table has Severity column (critical/moderate/low) + "compare every gap against every other before assigning Severity" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle" |
| C-11 | PASS | Vocabulary list enumerated in role block, not bare label |
| C-12 | PASS | "Current practice: [describe what this team currently does...]" + "Known failure mode: [describe the recurring failure...]" — both named fields in role block |
| C-13 | PASS | "Write a table with four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four columns named |
| C-14 | PASS | Gap table placed BEFORE phases: "Before tracing any phase, create your gap table now… Print the header row; leave every data row blank. Do not pre-fill any row. You will return to fill this table only after completing all four phases. When you return, compare every gap against every other before assigning Severity." — front-loaded empty skeleton with do-not-pre-fill guard and return instruction; C-14 activates on prose path via structural placement, not template field syntax |
| C-15 | PASS | No template field syntax (no check-N:, step-N:, gap-N: colon fields); C-12 satisfied (named fields in role block), C-13 satisfied (columns named), dual disqualifiers present; front-loaded gap table as prose table instruction is not "template apparatus" — apparatus exclusion is colon-notation field syntax only; C-14 and C-15 coexist |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Per-phase labeled sections (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK) exceed single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails; C-14 and C-16 cannot coexist |
| C-19 | PASS | Contextual disqualifier names specific deficiency ("names no specific condition") |
| C-20 | PASS | Domain vocabulary anchors disqualifier ("Confirm the environment is healthy") |
| C-21 | FAIL | Phase headers are labeled sections (PRE-DEPLOY CHECKS, etc.), not bare colloquial interrogatives |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | No incident narrative in role block |
| C-24 | FAIL | Template-path criterion — no skeleton structure |
| C-25 | PASS | No incident narrative; non-inertia domain-vocabulary framing; path-agnostic |
| C-26 | FAIL | No interrogative phase headers |
| C-27 | FAIL | Rollback section: "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" — prose instruction, not colon-notation fields (trigger:, rollback-1:, verify-rollback:) |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier in PRE-DEPLOY: *"'Confirm the environment is healthy' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier in POST-DEPLOY: *"A validation that asks 'did everything land correctly?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, PRE-DEPLOY) and C-30 (question-form, POST-DEPLOY VALIDATION) — phase-position differentiation present; both forms in distinct phase sections |
| C-32 | FAIL | Per-phase labeled sections exceed single-paragraph-per-phase density; C-31 achieved but not at compressed density |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-25, C-29, C-30, C-31 = 13 × 5 = 65 pts
**Score**: 60 + 30 + 65 = **155/210** | Delta from R15 standard prose baseline (150): +5 (C-14 activates on prose path) | Delta predicted: between best-case (+10) and worst-case (-10) — realized: C-14 PASS + C-15 PASS, no mutual exclusion

---

### V-02: Bare interrogative phase headers in prose — C-21/C-26 probe at standard density

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is stable' names no specific condition and does not qualify" — declarative disqualifier; 3+ checks with condition + failure enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency — the step that must complete before the next can begin and what breaks if it does not" |
| C-03 | PASS | "A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "Identify at least one gap per phase; state what should be added or changed" |
| C-06 | PASS | Ordering dependency explicit: "the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "state what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap summary table + Severity column + "Compare all gaps before assigning Severity" |
| C-10 | PASS | "Identify at least one automation hook" |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: [...checklist, deployment sequence, approval gates as practiced]" + "Known failure mode: [...]" — both named fields in role block |
| C-13 | PASS | "cross-phase gap summary table: Phase | Gap | Severity (critical / moderate / low) | Why" — all four columns named |
| C-14 | FAIL | Gap table appears as trailing instruction ("After all four phases, produce a cross-phase gap summary table"), not front-loaded before Phase 1 |
| C-15 | PASS | Prose achieves C-12 (named-fields baseline in role block), C-13 (named columns + comparison mandate), dual disqualifiers; no template field syntax; interrogative headers are prose section markers, not colon-notation fields — apparatus exclusion does not apply |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Bare interrogative headers create per-phase section structure ("what needs to be true before we touch this?" followed by content, then next header); sections exceed single-paragraph-per-phase density |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | PASS | Bare colloquial interrogative phase headers present: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" — exact surface form matches C-21 criterion; C-21 is a surface-form criterion, not template-context-dependent; the headers activate regardless of surrounding structure |
| C-22 | FAIL | No template field labels (no check-N:, step-N:, gap-N: fields) |
| C-23 | FAIL | No incident narrative in role block |
| C-24 | FAIL | Template-path criterion — no bare-label skeleton structure |
| C-25 | PASS | No incident narrative; path-agnostic |
| C-26 | PASS | Interrogative phase headers present — C-26 is a surface-form criterion; activates wherever interrogative headers appear, not template-context-exclusive |
| C-27 | FAIL | Rollback section is prose instruction, not three colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under "what needs to be true before we touch this?": *"'Verify the environment is stable' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under "did it land?": *"A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy section) and C-30 (question-form, post-deploy section) — phase-position differentiation via distinct interrogative header sections |
| C-32 | FAIL | Per-section structure (even with interrogative headers) exceeds single-paragraph-per-phase density |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31 = 14 × 5 = 70 pts
**Score**: 60 + 30 + 70 = **160/210** | Delta from R15 standard prose baseline: +10 (C-21 + C-26 both activate as surface-form criteria) | Delta predicted: = predicted (matches "150 to 160" hypothesis)

---

### V-03: Compressed prose + three-field rollback in prose — C-27 probe

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'ensure services are available' names no condition and does not qualify" — declarative disqualifier; "3+ checks, each naming the specific condition verified and what failure looks like" |
| C-02 | PASS | "list 4+ ordered steps and call out one ordering dependency explicitly — the step that must complete before the next begins" |
| C-03 | PASS | "a validation that asks 'did the deployment succeed?' names no probe or threshold and does not qualify" — question-form disqualifier; "2+ probes or thresholds" |
| C-04 | PASS | "for rollback cover exactly three labeled components in order — trigger (...), steps (...), verify (...)" |
| C-05 | PASS | "Per phase name one gap and its remedy" |
| C-06 | PASS | "call out one ordering dependency explicitly — the step that must complete before the next begins" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "its remedy" per gap |
| C-09 | PASS | Gap table + "compare each gap against the others before assigning Severity" |
| C-10 | PASS | "name at least one automation hook" |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: [what this team currently does — checklist, sequence, approval gates as practiced]" + "Known failure mode: [...]" in role block |
| C-13 | PASS | "(Phase, Gap, Severity, Why)" — four columns named |
| C-14 | FAIL | Gap table is trailing ("Close with a cross-phase gap table"), not front-loaded before Phase 1 |
| C-15 | PASS | Single-paragraph prose satisfies C-12 (named-fields baseline), C-13 (named columns + comparison mandate), dual disqualifiers; no template field syntax |
| C-16 | FAIL | No template field architecture |
| C-17 | PASS | All four phases in one flowing compressed instruction paragraph: "Trace the deployment of {{TOPIC}} in a single instruction: for pre-deploy… for sequence… for validation… for rollback… Per phase name one gap… Close with…" — single-paragraph-per-phase density or less; all C-15 requirements satisfied at compressed density |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | FAIL | No interrogative phase headers (inline "for pre-deploy…", "for sequence…" are structural clauses within one paragraph, not bare colloquial question headers) |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | No incident narrative |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | No incident narrative; path-agnostic |
| C-26 | FAIL | No interrogative headers |
| C-27 | FAIL | "exactly three labeled components in order — trigger (what condition initiates rollback), steps (what you undo and in what order), verify (how you confirm rollback succeeded)" — prose-parenthetical labeling; C-27 criterion specifies colon-notation fields (trigger:, rollback-1:, verify-rollback:); "fields" language is load-bearing; parenthetical labels in prose instruction do not constitute template fields; C-27 is template-exclusive |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier in pre-deploy clause: *"'ensure services are available' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier in validation clause: *"a validation that asks 'did the deployment succeed?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy clause) and C-30 (question-form, validation clause) — positional differentiation within compressed paragraph |
| C-32 | PASS | C-31 achieved within single instruction paragraph covering all four phases; density-independence confirmed; C-27 probe has no effect on density threshold |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-25, C-29, C-30, C-31, C-32 = 14 × 5 = 70 pts
**Score**: 60 + 30 + 70 = **160/210** | Delta from R15 compressed prose ceiling: 0 (C-27 template-exclusive confirmed; no gain) | Delta predicted: = predicted

---

### V-04: C-14 + C-21/C-26 joint — standard density, dual disqualifiers

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is stable' names no specific condition and does not qualify" — declarative disqualifier; 3+ checks enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency — the step that must complete before the next can begin and what breaks if it does not" |
| C-03 | PASS | "A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "Return to the gap table. Fill one row per phase" — one gap per phase enforced |
| C-06 | PASS | Ordering dependency explicit: "the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "state what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table Severity column + "compare every gap against the others before assigning Severity" |
| C-10 | PASS | "Identify at least one automation hook" |
| C-11 | PASS | Vocabulary list in role block |
| C-12 | PASS | "Current practice: [shared runbook, approval gates, deployment sequence as practiced]" + "Known failure mode: [...]" — both named fields in role block |
| C-13 | PASS | "Four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four named |
| C-14 | PASS | Gap table front-loaded before phases: "Before tracing any phase, write your gap table now. Four columns: Phase | Gap | Severity… Print the header row; leave all data rows blank. Do not pre-fill. Return to fill it only after all four phases are complete; compare every gap against the others before assigning Severity." — front-loaded empty skeleton with do-not-pre-fill guard and return instruction |
| C-15 | PASS | No template field syntax; C-12 and C-13 satisfied (named fields in role block, columns named), dual disqualifiers present; neither front-loaded prose gap table nor interrogative headers constitute template apparatus — colon-notation field syntax is the exclusive apparatus disqualifier; C-14, C-15, C-21, and C-26 all coexist |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Interrogative section headers ("what needs to be true before we touch this?", etc.) create per-phase section structure exceeding single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | PASS | Bare colloquial interrogative phase headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" — surface-form activation confirmed by V-02; joint activation with C-14 and C-15 confirmed here |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | No incident narrative |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | No incident narrative; path-agnostic |
| C-26 | PASS | Interrogative phase headers present — surface-form activation confirmed; joint activation with C-14, C-15, C-21 confirmed |
| C-27 | FAIL | Rollback section is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under "what needs to be true before we touch this?": *"'Verify the environment is stable' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under "did it land?": *"A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy section) and C-30 (question-form, post-deploy section) — phase-position differentiation via interrogative header sections |
| C-32 | FAIL | Per-section structure exceeds single-paragraph-per-phase density |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31 = 15 x 5 = 75 pts
**Score**: 60 + 30 + 75 = **165/210** | Delta from R15 prose ceiling (160): +5 (C-14 + C-21 + C-26 joint activation; C-15 survives; prose ceiling ties template ceiling) | Delta predicted: exceeded (hypothesis max was 160; realized 165 — C-14 joint with C-21/C-26 was not in the predicted range)

---

### V-05: C-21/C-26 + C-27 + compression tradeoff — INCOMPLETE

**Status**: No prompt specified (trace artifact: placeholder only). Structural analysis only.

V-05 faces a fundamental architectural contradiction: C-21 and C-26 require interrogative section headers as structural markers; C-17 and C-32 require single-paragraph compression with no section markers. These are mutually exclusive structural choices. A prompt that uses interrogative headers cannot simultaneously compress all phases into one paragraph — the headers create section breaks that invalidate the compression criterion. V-05 is not scoreable as designed; the "tradeoff" is structurally unresolvable within a single variation. This confirms the ceiling analysis: the two routes to 165/210 (compression path and structural-adoption path) are mutually exclusive by construction.

**Score**: N/A

---

## Scorecard summary

| Rank | Variation | Score | Delta from R15 | Path | Confirmed |
|------|-----------|-------|----------------|------|-----------|
| 1 | V-04 | **165/210** | +5 from prose ceiling | prose-standard + joint structural adoption | C-14 + C-21 + C-26 + C-15 coexist |
| 2 | V-02 | **160/210** | +10 from standard baseline | prose-standard + interrogative headers | C-21 + C-26 surface-form confirmed |
| 2 | V-03 | **160/210** | 0 (no change from compressed ceiling) | prose-compressed | C-27 template-exclusive confirmed |
| 4 | V-01 | **155/210** | +5 from standard baseline | prose-standard + front-loaded gap table | C-14 prose activation confirmed |
| — | V-05 | N/A | — | structural contradiction | C-17 incompatible with C-21/C-26 confirmed |

---

## R16 discriminating questions answered

**1. Does C-14 activate on the prose path?**
Yes — confirmed. V-01 and V-04 both show C-14 activating when a gap table instruction is placed before the phases with the do-not-pre-fill guard and return instruction. The enabling mechanism is structural placement (gap table before Phase 1), not template field syntax. C-14 is a placement criterion, not an apparatus criterion.

**2. Do C-14 and C-15 coexist on the prose path?**
Yes — confirmed. V-01 (155) and V-04 (165) both show C-14 PASS + C-15 PASS simultaneously. The apparatus exclusion in C-15 applies only to colon-notation field syntax (check-N:, step-N:, gap-N:). A front-loaded prose gap table is a structural instruction, not template apparatus. C-15 is apparatus-agnostic to table placement.

**3. Are C-21 and C-26 surface-form criteria or template-exclusive?**
Surface-form — confirmed. V-02 shows C-21 and C-26 both activating in a prose context where no template fields are present. The criteria activate wherever the interrogative header text appears: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" The "(template-path criterion)" label in R15 scorecards was shorthand for "not attempted on prose path" — not a logical exclusion.

**4. Is C-27 template-exclusive?**
Yes — confirmed. V-03 places three sequentially labeled rollback components in prose ("trigger (what condition initiates rollback), steps (what you undo and in what order), verify (how you confirm rollback succeeded)") and C-27 still FAILS. The "fields" language in C-27's criterion text is load-bearing: colon-notation syntax (trigger:, rollback-1:, verify-rollback:) is required. Parenthetical prose labels do not activate C-27.

**5. Does the prose ceiling rise above 160/210?**
Yes — to 165/210, tying the template ceiling. V-04 demonstrates that joint prose structural adoption (C-14 + C-21 + C-26 coexisting with C-15) adds 5 pts to the compressed-prose ceiling. Both routes to 165 are now confirmed: the compression route (C-15 + C-17 + C-32 + C-29–C-31) and the structural-adoption route (C-14 + C-15 + C-21 + C-26 + C-29–C-31). These routes are mutually exclusive (C-17 incompatible with C-21/C-26) but each reaches 165/210 independently.

**6. Can any path exceed 165/210?**
No — ceiling is confirmed at 165/210. The compression route yields 15 passing aspirationals (ceiling: 165). The structural-adoption route yields 15 passing aspirationals (ceiling: 165). No configuration activates 16 or more simultaneously: the criteria that differ between the two routes (C-17/C-32 vs C-21/C-26/C-14) are architecturally incompatible within a single prompt. Rubric v12 is fully characterized: no variation on either path can exceed 165/210. The ceiling is shared.

---

## Excellence signals (top variation: V-04)

**What V-04 achieved that no prior variation had reached:**

1. **Joint prose structural adoption: C-14 + C-21 + C-26 + C-15 all coexist.** The critical insight is that template structural patterns (front-loaded placement, interrogative header form) are separable from template apparatus (colon-notation field syntax). A prose prompt can adopt the structural benefits of templates without triggering apparatus exclusion in C-15. This was not attempted in any prior round.

2. **Prose ceiling converges with template ceiling at 165/210.** The template path and the optimal prose path now share the same maximum score through entirely different mechanism sets. The template path achieves this via field architecture (C-14, C-16, C-18, C-21, C-22, C-24, C-26, C-27, C-28). The prose path achieves it via structural adoption + disqualifier coverage (C-14, C-15, C-21, C-26, C-19, C-20, C-25, C-29, C-30, C-31). Neither path has access to the other's exclusive criteria at a net scoring advantage.

3. **C-27 is the lone template-exclusive criterion that matters.** Among the template criteria absent from the best prose path, only C-27 (three-field rollback structure), C-22, C-24, and C-28 are truly template-exclusive. C-27 alone is the structural remnant of template distinctiveness, and even with it the template path only ties the prose path.

---

## New patterns

**Pattern 1: prose-path-structure-adoption**
Template structural patterns (front-loaded gap table placement, bare interrogative phase headers) can be adopted in prose prompts without activating apparatus exclusion in C-15. Apparatus exclusion applies only to colon-notation field syntax (check-N:, step-N:, gap-N:). Structural adoption enables the prose path to achieve C-14 + C-21 + C-26 simultaneously alongside C-15, reaching 165/210. This pattern should be the default design choice for standard-density prose prompts targeting maximum score.

**Pattern 2: prose-ceiling-template-ceiling-convergence**
Rubric v12 prose ceiling = template ceiling = 165/210. The two routes to this ceiling are architecturally incompatible (compression blocks interrogative headers; interrogative headers block compression) but each independently reaches 165/210. Rubric v12 is fully characterized: no variation on either path can exceed 165/210. The rubric's discriminating range is complete; C-33 would require a new dimension not covered by any existing criteria cluster.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["prose-path-structure-adoption: front-loaded gap tables and interrogative phase headers activate C-14/C-21/C-26 in prose without triggering C-15 apparatus exclusion — colon-notation field syntax is the exclusive disqualifier", "prose-ceiling-template-ceiling-convergence: rubric v12 is fully characterized at 165/210 on both paths; two mutually exclusive routes (compression vs structural adoption) each reach the same ceiling; no variation can exceed 165/210"]}
```
