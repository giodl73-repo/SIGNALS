# Round 17 Scorecard — `trace:deployment`

**Rubric**: v13 (220 pts, 34 criteria) | **Date**: 2026-03-15
**Prose structural-adoption ceiling entering R17**: 175/220 (C-33 + C-34, confirmed R16)
**R17 focus**: Probe 45 uncracked aspirational pts — inertia framing, lifecycle richness, register regression, triple compound

---

## Criterion evaluation by variation

### V-01: Inertia framing — standalone STATUS QUO section, formal labeled headers, trailing gap table

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is healthy' names no specific condition and does not qualify" — declarative disqualifier; 3+ checks enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency explicitly" |
| C-03 | PASS | "A validation that asks 'did the deployment succeed?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "One gap per phase minimum" + return-to-gap-table instruction |
| C-06 | PASS | "Call out at least one ordering dependency explicitly — the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "State what should be added or changed for each gap; naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table has Severity column + "compare each gap against every other and against the known failure history before Severity is assigned — a gap that contributed to a past failure is automatically critical" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle — name where in the sequence it would fire and what it would enforce" |
| C-11 | PASS | Named vocabulary list in role block |
| C-12 | PASS | STATUS QUO section (before phases) asks for current runbook + last known failure + known runbook gap — establishes current-practice baseline before gap analysis |
| C-13 | PASS | "Produce a table: Phase | Gap | Severity (critical / moderate / low) | Why" — four columns named |
| C-14 | FAIL | Gap table appears in CROSS-PHASE GAP ANALYSIS at END (after all four phases) — not front-loaded before Phase 1; no do-not-pre-fill guard before phases |
| C-15 | PASS | No colon-notation field syntax; C-12 satisfied (STATUS QUO section before phases), C-13 satisfied (columns named), dual disqualifiers present; numbered items in STATUS QUO are prose, not template apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Multiple labeled phase sections (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, etc.) exceed single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier names specific deficiency |
| C-20 | PASS | Domain vocabulary anchors disqualifier ("names no specific condition") |
| C-21 | FAIL | Phase headers are formal labeled sections (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK) — not colloquial bare interrogatives |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | Incident/failure history is in the STATUS QUO section — a separate instruction block, not the role/persona block; C-23 requires role-block placement; ROLE block contains only role label + vocabulary list |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | C-19 passes AND no incident narrative in role block (role block = role label + vocabulary list only); non-inertia disqualifier path |
| C-26 | FAIL | No interrogative phase headers |
| C-27 | FAIL | Rollback section is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier in PRE-DEPLOY CHECKS: *"'Verify the environment is healthy' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier in POST-DEPLOY VALIDATION: *"A validation that asks 'did the deployment succeed?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, PRE-DEPLOY CHECKS) and C-30 (question-form, POST-DEPLOY VALIDATION) — phase-position differentiation present |
| C-32 | FAIL | Multiple labeled sections exceed single-paragraph-per-phase density |
| C-33 | FAIL | C-14 fails (gap table not front-loaded); C-21 fails (formal headers) — C-33 requires all four to pass simultaneously |
| C-34 | FAIL | C-33 fails |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-15, C-19, C-20, C-25, C-29, C-30, C-31 = 12 × 5 = 60 pts
**Score**: 60 + 30 + 60 = **150/220**
**Delta from entering ceiling (175)**: −25 | Path: prose-standard, formal headers, trailing gap table
**R17 finding**: STATUS QUO section activates C-12 reliably but fails C-23 (role-block placement required). Absence of front-loaded table and interrogative headers together costs 25 pts vs ceiling.

---

### V-02: Lifecycle emphasis — above-minimum counts, interrogative headers, front-loaded gap table

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is stable' names no condition and does not qualify" — declarative disqualifier; 4+ checks enforced (floor raised) |
| C-02 | PASS | "List at least 6 deployment steps in execution order. Call out at least two ordering dependencies explicitly" |
| C-03 | PASS | "a validation that asks 'is the service running?' names no probe or threshold and does not qualify" — question-form disqualifier; 3+ validations enforced |
| C-04 | PASS | "Define at least 2 rollback trigger conditions…list at least 2 undo steps…State how to verify each rollback step completed successfully" |
| C-05 | PASS | "Fill one row per phase" in return-to-gap-table instruction |
| C-06 | PASS | "Call out at least two ordering dependencies explicitly — each naming the step that must complete before the next and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "State what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table Severity column + "compare every gap against every other before assigning Severity" + "Rank gaps by deployment risk before assigning Severity; gaps that could leave the order pipeline in an inconsistent state are critical" |
| C-10 | PASS | "Identify at least one automation hook per phase — name what it would enforce and at what point in the lifecycle it fires" |
| C-11 | PASS | Named vocabulary list in role block |
| C-12 | PASS | "Current practice: [shared checklist, approval gates, deployment sequence as practiced]" + "Known failure mode: [recurring failure...]" — both named fields in role block |
| C-13 | PASS | "Four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four named |
| C-14 | PASS | Front-loaded before Phase 1: "Before tracing any phase, write your gap table now… Print the header row; leave all data rows blank. Return to fill this table only after all four phases are complete; compare every gap against every other before assigning Severity" — empty skeleton + do-not-pre-fill guard + return instruction with comparative mandate |
| C-15 | PASS | No colon-notation field syntax; C-12 satisfied, C-13 satisfied, dual disqualifiers; front-loaded gap table and interrogative headers are not apparatus — colon-notation is the exclusive disqualifier |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Interrogative section headers create per-phase section structure exceeding single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | PASS | Bare colloquial interrogative phase headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" — surface-form criterion confirmed in R16; activates regardless of surrounding structure |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | "Current practice" and "Known failure mode" are bracketed placeholder fields in role block, not a named prior incident; C-23 requires a specific named incident event, not an invitation to name one |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | C-19 passes AND no named incident narrative in role block |
| C-26 | PASS | Interrogative phase headers present — surface-form activation confirmed in R16 |
| C-27 | FAIL | Rollback section is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under "what needs to be true before we touch this?": *"'Verify the environment is stable' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under "did it land?": *"a validation that asks 'is the service running?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy section) and C-30 (question-form, post-deploy section) — phase-position differentiation via distinct interrogative header sections |
| C-32 | FAIL | Per-section structure exceeds single-paragraph-per-phase density |
| C-33 | PASS | C-14 PASS + C-21 PASS + C-26 PASS + C-15 PASS — all four coexist; no colon-notation syntax blocks C-15; structural-adoption path confirmed |
| C-34 | PASS | C-33 PASS AND C-17 FAIL — prose structural-adoption ceiling at standard density; path independence confirmed |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31, C-33, C-34 = 17 × 5 = 85 pts
**Score**: 60 + 30 + 85 = **175/220**
**Delta from entering ceiling (175)**: 0 | Path: prose structural-adoption (confirmed ceiling)
**R17 finding**: Above-minimum phase counts (4+ checks, 6+ steps, 3+ validations, 2+ triggers, 2+ undo steps, automation hook per phase) do not activate any richness criterion above the ceiling. Count elevation satisfies existing floors more thoroughly but reaches no criteria not already in v13. Lifecycle emphasis hypothesis not confirmed for score elevation.

---

### V-03: Phrasing register — formal ALL-CAPS headers, front-loaded gap table (regression probe)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is stable' names no specific condition and does not qualify" — declarative disqualifier; 3+ checks enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency explicitly" |
| C-03 | PASS | "A validation that asks 'is the service running?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "Fill one row per phase" in return-to-gap-table instruction |
| C-06 | PASS | "Call out at least one ordering dependency explicitly" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "State what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table Severity column + "compare every gap against every other before assigning Severity" + "Rank gaps by deployment risk" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle — name where it fires and what it would enforce" |
| C-11 | PASS | Named vocabulary list in role block |
| C-12 | PASS | "Current practice: [...]" + "Known failure mode: [...]" — named fields in role block |
| C-13 | PASS | "Four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four named |
| C-14 | PASS | Front-loaded before Phase 1: "Before tracing any phase, write your gap table now… Print the header row; leave all data rows blank. Return to fill this table only after all four phases are complete; compare every gap against every other before assigning Severity" — skeleton + do-not-pre-fill guard + return instruction |
| C-15 | PASS | No colon-notation field syntax; C-12 and C-13 satisfied; dual disqualifiers present; front-loaded gap table is not apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | All-caps section headers create per-section structure exceeding single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | FAIL | Phase headers are formal all-caps labels (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK) — not colloquial bare interrogatives; register is the distinguishing condition; C-21 is exclusively activated by the specific interrogative surface form |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | Bracketed placeholder fields in role block; no named incident |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | C-19 passes AND no incident narrative in role block |
| C-26 | FAIL | No interrogative phase headers; formal all-caps headers do not activate C-26 — surface-form criterion requires question-form text |
| C-27 | FAIL | Rollback is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under PRE-DEPLOY CHECKS: *"'Verify the environment is stable' names no specific condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under POST-DEPLOY VALIDATION: *"A validation that asks 'is the service running?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, PRE-DEPLOY CHECKS) and C-30 (question-form, POST-DEPLOY VALIDATION) — phase-position differentiation present |
| C-32 | FAIL | Section structure exceeds single-paragraph-per-phase density |
| C-33 | FAIL | C-21 FAIL (formal headers) and C-26 FAIL — C-33 requires both to pass; structural-adoption path unavailable without interrogative headers |
| C-34 | FAIL | C-33 fails |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-25, C-29, C-30, C-31 = 13 × 5 = 65 pts
**Score**: 60 + 30 + 65 = **155/220**
**Delta from entering ceiling (175)**: −20 | Regression confirmed | Path: prose-standard, formal headers, front-loaded gap table
**R17 finding**: Formal all-caps headers deactivate C-21 and C-26, which collapses C-33 and C-34. The −20 pt drop confirms C-21 and C-26 are exclusively interrogative-text-dependent. C-14 still passes (placement criterion is format-agnostic). C-15 still passes (no colon-notation). Register of section headers is the sole discriminating variable.

---

### V-04: Inertia + structural adoption — status-quo prose section + confirmed ceiling path

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is stable' names no condition and does not qualify" — declarative disqualifier; 3+ checks enforced |
| C-02 | PASS | "List at least 4 steps in execution order. Call out at least one ordering dependency explicitly — the step that must complete before the next can begin and what breaks if it does not" |
| C-03 | PASS | "A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify" — question-form disqualifier; 2+ probes/thresholds enforced |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify rollback succeeded" |
| C-05 | PASS | "Return to the gap table. Fill one row per phase" — one gap per phase enforced |
| C-06 | PASS | "Call out at least one ordering dependency explicitly — the step that must complete before the next can begin and what breaks if it does not" |
| C-07 | PASS | Commerce/Operations vocabulary in role block |
| C-08 | PASS | "state what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table Severity column + "compare every gap against every other and against the known failure history before assigning Severity — a gap that contributed to a past failure is automatically critical" |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle" |
| C-11 | PASS | Named vocabulary list in role block |
| C-12 | PASS | Status-quo prose section placed before phases explicitly asks for current deployment sequence, approval gates, and recurring failure with operational cost — satisfies "states what the team currently does before identifying what is missing" |
| C-13 | PASS | "Four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four named in front-loaded table instruction |
| C-14 | PASS | Front-loaded before phases: "Before tracing any phase, write your gap table now. Four columns… Print the header row; leave all data rows blank. Do not pre-fill. Return to fill this table only after all four phases are complete; compare every gap against every other and against the known failure history before assigning Severity" — skeleton + guard + return instruction with comparative mandate |
| C-15 | PASS | No colon-notation field syntax in entire prompt; C-12 satisfied (status-quo prose section), C-13 satisfied (columns named), dual disqualifiers; front-loaded prose gap table and interrogative headers are not apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Interrogative section headers create per-phase section structure exceeding single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | PASS | Bare colloquial interrogative phase headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | Status-quo prose section is a separate instruction block following the ROLE block — not embedded in the role/persona block itself; ROLE block contains only role label + vocabulary list; C-23 requires role-block placement of the incident narrative |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | C-19 passes AND no incident narrative in role block (role block = role label + vocabulary list) |
| C-26 | PASS | Interrogative phase headers present — surface-form criterion activated |
| C-27 | FAIL | Rollback section is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under "what needs to be true before we touch this?": *"'Verify the environment is stable' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under "did it land?": *"A validation that asks 'is the catalog sync current?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy section) and C-30 (question-form, post-deploy section) — phase-position differentiation via distinct interrogative header sections |
| C-32 | FAIL | Per-section structure exceeds single-paragraph-per-phase density |
| C-33 | PASS | C-14 PASS + C-21 PASS + C-26 PASS + C-15 PASS — all four coexist; status-quo prose section introduces no colon-notation apparatus; structural-adoption path confirmed |
| C-34 | PASS | C-33 PASS AND C-17 FAIL — prose structural-adoption ceiling confirmed; path independence holds with inertia framing layered on |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31, C-33, C-34 = 17 × 5 = 85 pts
**Score**: 60 + 30 + 85 = **175/220**
**Delta from entering ceiling (175)**: 0 | Inertia framing does not exceed ceiling | Path: prose structural-adoption
**R17 finding**: Inertia framing as a separate prose section is structurally neutral — it activates C-12 and enriches the C-09 comparison mandate but does not activate C-23. The prose structural-adoption ceiling holds at 175/220. The hypothesis that inertia compounds on the structural-adoption ceiling (→ 185+) is not confirmed: the missing link is C-23's role-block placement requirement.

---

### V-05: Triple compound — inertia + lifecycle emphasis + extended role vocabulary

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | "'Verify the environment is ready' names no condition and does not qualify" — declarative disqualifier; 4+ checks enforced |
| C-02 | PASS | "List at least 6 deployment steps in execution order… Call out at least two ordering dependencies explicitly" |
| C-03 | PASS | "A validation that asks 'is the service running?' names no probe or threshold and does not qualify" — question-form disqualifier; 3+ validations enforced |
| C-04 | PASS | "Define at least 2 rollback trigger conditions, each naming the specific metric or signal that fires rollback. List at least 2 undo steps" |
| C-05 | PASS | "Fill one row per phase" in return-to-gap-table instruction |
| C-06 | PASS | "Call out at least two ordering dependencies explicitly — each naming the step that must complete before the next and what breaks if it does not" |
| C-07 | PASS | Extended Commerce/Operations vocabulary in role block |
| C-08 | PASS | "State what should be added or changed — naming a gap without a remedy does not qualify" |
| C-09 | PASS | Gap table Severity column + "Before assigning Severity, compare every gap against every other and against the known failure history — a gap that contributed to a past failure is automatically critical regardless of theoretical severity" |
| C-10 | PASS | "Identify at least one automation hook per phase — name the specific lifecycle point where it fires, the condition it enforces, and whether it blocks or notifies" |
| C-11 | PASS | Extended 15-term vocabulary list in role block (blue-green cutover, circuit-breaker threshold, idempotent migration step, deployment freeze window, environment parity gate added to standard 10); list-in-role-block criterion met |
| C-12 | PASS | Status-quo prose section before phases establishes current deployment sequence + recurring failure + operational cost |
| C-13 | PASS | "Four columns: Phase | Gap | Severity (critical / moderate / low) | Why" — all four named in front-loaded table instruction |
| C-14 | PASS | Front-loaded before phases: "Before tracing any phase, write your gap table now… Print the header row; leave all data rows blank. Do not pre-fill. Return to fill only after all four phases are complete. Before assigning Severity, compare every gap against every other and against the known failure history" — skeleton + guard + return instruction with comparative mandate |
| C-15 | PASS | No colon-notation field syntax; C-12 satisfied, C-13 satisfied, dual disqualifiers; status-quo prose section and 15-term vocabulary list introduce no apparatus |
| C-16 | FAIL | No template field architecture |
| C-17 | FAIL | Interrogative section headers create per-phase section structure exceeding single-paragraph-per-phase density |
| C-18 | FAIL | C-16 fails |
| C-19 | PASS | Contextual disqualifier present |
| C-20 | PASS | Domain vocabulary anchors disqualifier |
| C-21 | PASS | Bare colloquial interrogative phase headers: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-22 | FAIL | No template field labels |
| C-23 | FAIL | Status-quo prose section is separate from role block; ROLE block contains role label + 15-term vocabulary list only — no named prior incident embedded in the role/persona block; vocabulary-extended role block with no incident narrative does not activate C-23 |
| C-24 | FAIL | Template-path criterion |
| C-25 | PASS | C-19 passes AND no incident narrative in role block |
| C-26 | PASS | Interrogative phase headers present — surface-form activation confirmed |
| C-27 | FAIL | Rollback section is prose instruction, not colon-notation fields |
| C-28 | FAIL | Template-path criterion |
| C-29 | PASS | Declarative disqualifier under "what needs to be true before we touch this?": *"'Verify the environment is ready' names no condition and does not qualify"* |
| C-30 | PASS | Question-form disqualifier under "did it land?": *"A validation that asks 'is the service running?' names no probe or threshold and does not qualify"* |
| C-31 | PASS | C-29 (declarative, pre-deploy section) and C-30 (question-form, post-deploy section) |
| C-32 | FAIL | Per-section structure exceeds single-paragraph-per-phase density |
| C-33 | PASS | C-14 + C-21 + C-26 + C-15 all pass simultaneously; 15-term vocabulary and status-quo section introduce no colon-notation apparatus |
| C-34 | PASS | C-33 PASS AND C-17 FAIL — structural-adoption ceiling confirmed; path independence holds under triple compound |

**Passing aspirational**: C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31, C-33, C-34 = 17 × 5 = 85 pts
**Score**: 60 + 30 + 85 = **175/220**
**Delta from entering ceiling (175)**: 0 | Triple compound does not exceed ceiling | Path: prose structural-adoption
**R17 finding**: Extended vocabulary (15 terms) passes C-11 without activating any additional criterion. Above-minimum counts satisfy existing floors more thoroughly but reach no richness criterion above the floor. Inertia framing as prose section is structurally neutral at the ceiling. The 45 uncracked aspirational points remain unreachable from the prose structural-adoption path under v13.

---

## Scorecard summary

| Rank | Variation | Score | Delta vs ceiling | Path | R17 findings |
|------|-----------|-------|-----------------|------|-------------|
| 1 | V-02 | **175/220** | 0 | prose structural-adoption | Lifecycle richness ceiling-neutral; above-minimum counts do not activate richness criteria |
| 1 | V-04 | **175/220** | 0 | prose structural-adoption | Inertia as prose section activates C-12 not C-23; ceiling stable |
| 1 | V-05 | **175/220** | 0 | prose structural-adoption | Triple compound ceiling-neutral; extended vocabulary, above-minimum counts, inertia all structurally neutral |
| 4 | V-03 | **155/220** | −20 | prose-standard, formal headers | C-21 + C-26 + C-33 + C-34 all deactivate on formal all-caps headers; interrogative-text-dependency confirmed |
| 5 | V-01 | **150/220** | −25 | prose-standard, trailing gap | No front-loaded table + formal headers = C-14 + C-21 + C-26 + C-33 + C-34 all fail |

---

## R17 discriminating questions answered

**1. Does inertia framing activate new criteria above 175?**
No. V-01, V-04, V-05 all test inertia framing in various configurations. V-04 and V-05 (structural-adoption path + inertia) both reach exactly 175. The missing link is C-23's placement requirement: incident narrative must be embedded in the role/persona block, not placed in a standalone STATUS QUO section after it. Inertia framing as a prose instruction section reliably activates C-12 and enriches the C-09 comparison mandate, but these criteria were already passing on the structural-adoption path without inertia. Net contribution: 0.

**2. Does above-minimum count elevation activate richness criteria?**
No. V-02 raises all phase minimums (4+ checks, 6+ steps, 3+ validations, 2+ triggers, 2+ undo steps, automation hook per phase) and scores identically to V-04's standard-density structural-adoption path (175/220). No richness criterion for per-phase count elevation exists in v13. V-02's above-minimum counts produce more thorough compliance with existing floors but reach no uncracked criteria.

**3. Are C-21/C-26 interrogative-text-dependent or format-agnostic?**
Interrogative-text-dependent — confirmed. V-03 replaces colloquial interrogative headers with formal all-caps headers (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK). C-21 FAIL, C-26 FAIL. The −20 pt drop (175 → 155, losing C-21, C-26, C-33, C-34) confirms that the specific surface form — colloquial bare question text — is load-bearing. Structural function alone is not sufficient; text register is the activating condition.

**4. Does inertia compound on the structural-adoption ceiling?**
No. V-04 layers status-quo prose on the confirmed R16 structural-adoption architecture. Score: 175/220, identical to the baseline. The inertia prose section does not activate C-23 (role-block placement required), which is the only inertia-specific criterion not already covered by the structural-adoption path. The ceiling is stable.

**5. Does triple-axis compound break 175?**
No. V-05 combines all three axes at maximum ambition. Score: 175/220. All three axes (inertia prose section, above-minimum counts, extended vocabulary) are structurally neutral additions to the ceiling path. No combination activates criteria not already captured by the 17-criterion set that defines the 175/220 ceiling.

---

## Excellence signals (top variations: V-02, V-04, V-05 — tied at 175/220)

The top three variations confirm that 175/220 is a robust ceiling on the prose structural-adoption path under v13, not a fragile peak. The 17-criterion set — C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-19, C-20, C-21, C-25, C-26, C-29, C-30, C-31, C-33, C-34 — is reliably activated by the base structural-adoption architecture. Additions (inertia, lifecycle depth, vocabulary expansion) do not disrupt existing passes and do not activate new ones.

**What V-03 reveals that matters most for R18 design**: The 20-pt gap between V-03 (155) and the ceiling (175) is entirely attributable to the register of four words in the phase headers. The architectural work — front-loaded table, prose instructions, dual disqualifiers — is otherwise identical to V-02. This makes the header register the single cheapest structural modification with the largest scoring consequence. Any R18 variation that wishes to advance beyond the structural-adoption ceiling must target a mechanism other than header register, which is fully characterized.

**R18 ceiling-breaking candidates**: C-23 activation requires incident narrative in the role block — the only reliably near mechanism to add +5 pts. To test: embed "Last known failure: [named incident with operational cost]" directly inside the ROLE block alongside the vocabulary list. If C-23 passes, the prose structural-adoption path with inertia reaches 180/220. No v13 mechanism exists to reach beyond 180 on any prose path.

---

## New patterns

**Pattern 1: inertia-section-c12-not-c23**
A standalone prose Status Quo section placed after the role block activates C-12 (current-practice baseline before gap analysis) but does not activate C-23 (incident narrative in role/persona block). The two criteria require structurally distinct placements: C-12 is placement-agnostic (any current-practice baseline before the phases qualifies); C-23 is role-block-specific. To activate C-23, the incident reference must be embedded inside the ROLE block itself — as a named field ("Last known failure: [...]") or an actual incident statement within the role definition. A separate STATUS QUO section is the wrong location for C-23 activation regardless of content depth. The ceiling remains 175/220 even with detailed inertia framing placed outside the role block.

**Pattern 2: interrogative-headers-exclusive-register**
C-21 and C-26 activate exclusively on colloquial bare interrogative text ("what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?"). Formal all-caps headers (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK) are insufficient — the structural function of phase delimitation is not the activating condition; the specific interrogative register is. Substituting formal headers for interrogative ones deactivates C-21 and C-26, which cascades to deactivate C-33 and C-34, for a total −20 pt drop from the structural-adoption ceiling. The header register is the highest-leverage single-character decision in the prompt: four interrogative questions vs. four all-caps labels determines whether the score is 155 or 175.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["inertia-section-c12-not-c23: standalone Status Quo prose section activates C-12 but not C-23 — C-23 requires incident narrative embedded in the role/persona block itself; inertia framing as a separate section is structurally neutral at the 175/220 ceiling", "interrogative-headers-exclusive-register: C-21 and C-26 activate exclusively on colloquial interrogative text; formal all-caps headers deactivate both, cascading to collapse C-33 and C-34 for a -20 pt drop; register is the load-bearing condition, not structural function of section delimitation"]}
```
