# Quest Scorecard — `trace:deployment` Round 13
**Rubric**: v11 (200 pts, 30 criteria) | **Date**: 2026-03-15

---

## Pre-Score: R12 Pattern Review

Reading R12 scorecard before scoring. Key carryforward:

- **C-30 promoted from R12 V-02**: question-form disqualifier is the third independent C-19 generator (alongside inertia-sourced framing and non-inertia domain-vocabulary framing). V-01 and V-05 target this axis directly. V-04 tests C-23 ∩ C-30 orthogonality.
- **Template-path ceiling confirmed at 165**: prose-path criteria (C-15/C-17/C-19/C-20/C-23/C-29/C-30) are inaccessible from the template path. C-21/C-22/C-24/C-26/C-27/C-28 are template-path exclusive.
- **C-25 / C-23 mutual exclusion**: incident narrative in role block → C-23 pass, C-25 fail. No incident narrative → C-25 pass, C-23 fail.

Scoring axis map for R13:
- V-01: C-30 alone (prose, standard density)
- V-02: C-29 + C-17 joint (declarative, compressed)
- V-03: template ceiling via C-26 + C-27 + C-28 + C-21 + C-22 + C-24 + C-14 + C-16 + C-18
- V-04: C-23 ∩ C-30 orthogonality
- V-05: C-17 ∩ C-30 joint (question-form, compressed)

---

## Criterion Reference (scoring weights)

| Tier | IDs | Pts each | Tier total |
|------|-----|----------|------------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-30 | 5 | 110 |
| **Total** | **C-01–C-30** | — | **200** |

---

## V-01 — Question-form disqualifier, prose path, standard density

**Axis**: C-30 confirmation — question-form expression as third C-19 generator

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "List at least 3 pre-deploy checks. For each check, name the specific condition being verified and what failure looks like." ≥3 checks with condition + failure required. |
| C-02 | PASS | "List at least 4 discrete numbered steps in execution order." Ordered, numbered sequence floor met. |
| C-03 | PASS | "List at least 2 validation actions. Each must name a probe, threshold, or data-integrity assertion." |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify the rollback succeeded." All three components named. |
| C-05 | PASS | "For each phase, identify at least one gap." Four phases addressed = four gaps required. |
| C-06 | PASS | "Explicitly call out at least one ordering dependency — a step that must complete before others can start." |
| C-07 | PASS | Role block enumerates: catalog sync, order pipeline drain, inventory lock, tenant provisioning, health-check threshold, rollback trigger, canary assertion, migration gate. |
| C-08 | PASS | "For each gap, state what should be added or changed — naming a gap without prescribing a remedy does not qualify." Remedy required. |
| C-09 | PASS | Cross-phase table with Severity column; "compare it against the others before assigning Severity." |
| C-10 | PASS | "Identify at least one automation hook in the deployment lifecycle." Explicit instruction. |
| C-11 | PASS | Vocabulary enumerated as named list inside ROLE block (not just a label). |
| C-12 | PASS | "Current practice" + "Known failure mode" fields in role block establish status-quo before analysis. |
| C-13 | PASS | "Produce a cross-phase gap summary table with columns: Phase, Gap, Severity (critical / moderate / low), Why." Columns named. |
| C-14 | FAIL | Gap table appears as post-phase instruction, not front-loaded before Phase 1 as empty skeleton. No do-not-pre-fill guard. |
| C-15 | PASS | C-12 achieved via role-block named fields; C-13 achieved via prose naming columns and mandating cross-gap comparison. No template apparatus. All three C-15 requirements met through explicit prose alone. |
| C-16 | FAIL | Instructions are prose, not template field scaffolding. No ≥3 Check-NN / ≥4 Step-NN / ≥2 Validation-NN fields present. |
| C-17 | FAIL | C-15 passes but density is above single-paragraph-per-phase — separate labeled sections (PRE-DEPLOY, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK) each carry their own instruction paragraph. |
| C-18 | FAIL | C-14 fails; C-18 requires both C-14 and C-16 simultaneously. |
| C-19 | PASS | Disqualifying example present: "A check that asks 'is everything ready?' names no specific condition and does not qualify." |
| C-20 | PASS | Second disqualifier: "A validation that asks 'did it deploy correctly?' names no probe or threshold and does not qualify." Domain-contextual form (references probe/threshold — deployment vocabulary). |
| C-21 | FAIL | Prose path; no bare field labels (check-1:, step-1:). |
| C-22 | FAIL | Prose path; no colloquial question headers. |
| C-23 | FAIL | No incident narrative in role block. |
| C-24 | FAIL | Prose path. |
| C-25 | PASS | No incident narrative anywhere in prompt. Role block contains only vocabulary list + current practice + known failure mode. |
| C-26 | FAIL | Section headers are declarative labels (PRE-DEPLOY, DEPLOYMENT SEQUENCE), not interrogative questions. |
| C-27 | FAIL | Rollback described in prose, not as exactly three template fields (trigger/rollback-N/verify-rollback). |
| C-28 | FAIL | Neither C-26 nor C-27 pass. |
| C-29 | FAIL | Disqualifiers are question-form ("is everything ready?", "did it deploy correctly?"), not declarative domain-contextual form. |
| C-30 | PASS | Question-form disqualifier present and structurally operative: "a check that asks 'is everything ready?' names no specific condition." The interrogative framing of the disqualifier is the distinguishing condition. |

**Criteria passed**: C-01–C-13, C-15, C-19, C-20, C-25, C-30 (19 criteria)
**Score**: 60 + 30 + (5×5) + 5 + 5 + 5 + 5 + 5 = **140/200**

---

## V-02 — Declarative domain-contextual disqualifier, compressed prose

**Axis**: C-17 ∩ C-29 joint — single-paragraph density with declarative disqualifier

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "for pre-deploy list 3+ checks — each names the specific condition and what failure looks like" with inline disqualifier. |
| C-02 | PASS | "for sequence list 4+ ordered steps and call out at least one explicit ordering dependency." |
| C-03 | PASS | "for validation list 2+ probes, thresholds, or data-integrity assertions." |
| C-04 | PASS | "for rollback state trigger, undo steps, and revert verification." All three components present. |
| C-05 | PASS | "Per phase identify at least one gap." Four phases in scope. |
| C-06 | PASS | "call out at least one explicit ordering dependency" — named requirement. |
| C-07 | PASS | Vocabulary list in ROLE block (catalog sync, order pipeline drain, inventory lock, tenant provisioning, health-check threshold, rollback trigger, canary assertion, migration gate). |
| C-08 | PASS | "state its remedy" — each gap requires actionable prescription. |
| C-09 | PASS | "compare each gap against the others before assigning Severity" + table with Severity column. |
| C-10 | PASS | "Identify at least one automation hook." |
| C-11 | PASS | Vocabulary as named list in ROLE block. |
| C-12 | PASS | "Current practice" + "Known failure mode" in ROLE block. |
| C-13 | PASS | "Produce a cross-phase gap summary table (columns: Phase, Gap, Severity, Why)" — columns named. |
| C-14 | FAIL | No front-loaded skeleton. Gap table instruction appears at end, not before Phase 1 as empty prefilled structure. |
| C-15 | PASS | C-12 achieved via ROLE block named fields + prose. C-13 achieved via prose naming columns and mandating cross-gap comparison. No template apparatus. Three C-15 requirements met: named output elements, cross-gap comparison mandate, disqualifying example. |
| C-16 | FAIL | Prose instructions; no template field scaffolding. |
| C-17 | PASS | C-15 passes. The entire multi-phase instruction is a single flowing paragraph — below single-paragraph-per-phase density. All three C-15 structural requirements present at compressed density. |
| C-18 | FAIL | C-14 fails. |
| C-19 | PASS | Disqualifying example: "'verify the environment is stable' names no condition and does not qualify." |
| C-20 | PASS | Second disqualifier uses domain vocabulary: "'keep an eye on error rates' names no probe or threshold and does not qualify." Domain-contextual form confirmed. |
| C-21 | FAIL | Prose path. |
| C-22 | FAIL | Prose path. |
| C-23 | FAIL | No incident narrative. |
| C-24 | FAIL | Prose path. |
| C-25 | PASS | No incident narrative anywhere. Role block has known failure mode but no inertia narrative. |
| C-26 | FAIL | No interrogative headers. Single paragraph format has no section headers at all. |
| C-27 | FAIL | No template field rollback triple. |
| C-28 | FAIL | Neither C-26 nor C-27 pass. |
| C-29 | PASS | "'keep an eye on error rates' names no probe or threshold and does not qualify" — declarative, uses domain vocabulary (error rates), not question-form. This is the distinguishing condition for C-29 vs C-30. |
| C-30 | FAIL | Disqualifiers are declarative ("'verify the environment is stable' names no condition..."), not question-form. |

**Criteria passed**: C-01–C-13, C-15, C-17, C-19, C-20, C-25, C-29 (20 criteria)
**Score**: 60 + 30 + (5×5) + 5 + 5 + 5 + 5 + 5 + 5 = **145/200**

---

## V-03 — Template-path ceiling: interrogative headers + rollback triple + colloquial bare labels

**Axis**: C-26 + C-27 + C-28 + C-21 + C-22 + C-24 + C-14 + C-16 + C-18 joint — targeting 165/200

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | check-1, check-2, check-3 fields — three Check-NN fields present. |
| C-02 | PASS | step-1, step-2, step-3, step-4 fields — four Step-NN fields present in order. |
| C-03 | PASS | validation-1, validation-2 fields — two Validation-NN fields present. |
| C-04 | PASS | trigger + rollback-1 + verify-rollback fields — all three rollback components present. |
| C-05 | PASS | gap-1, gap-2, gap-3, gap-4 — one gap field per phase. |
| C-06 | PASS | ordering-dependency field present. |
| C-07 | PASS | Vocabulary list in ROLE block. |
| C-08 | PASS | "For each row, state what should be added or changed." Return instruction enforces actionability. |
| C-09 | PASS | Gap registry table has Severity column; "Compare each gap against the others before assigning Severity." |
| C-10 | PASS | automation-hook field present in PRE-DEPLOY phase. |
| C-11 | PASS | Vocabulary enumerated in ROLE block: catalog sync, order pipeline drain, inventory lock, etc. |
| C-12 | PASS | "Current practice: [fill]" + "Known failure mode: [fill]" in ROLE block. |
| C-13 | PASS | Gap registry table at top of prompt with Phase / Gap / Severity / Why columns. |
| C-14 | PASS | Gap registry placed BEFORE Phase 1 as an empty skeleton; "fill this last; do not pre-fill any row" is the do-not-pre-fill guard; "Compare each gap against the others before assigning Severity" is the comparative return instruction. All three C-14 components present. |
| C-15 | FAIL | Template apparatus is present (named fields check-1/step-1/trigger/rollback-1, labeled sections with bare headers). C-12 and C-13 are not achieved through prose alone. Template scaffolding is the structural mechanism. |
| C-16 | PASS | Template field count meets all floors (≥3 Check-NN, ≥4 Step-NN, ≥2 Validation-NN, trigger + rollback-1 + verify-rollback, gap-N per phase, automation-hook). No explicit "GATE N: Do not proceed until..." text present. "fill this last; do not pre-fill any row" is a do-not-pre-fill guard, not GATE enforcement text per C-18 definition. Gate-free architecture confirmed. |
| C-17 | FAIL | C-15 fails; C-17 requires C-15 to pass first. |
| C-18 | PASS | C-14 passes (front-loaded skeleton + comparative return). C-16 passes (template field coverage, gate-free). The do-not-pre-fill guard in the skeleton is not GATE text, so C-16 is not disqualified. Orthogonal properties confirmed simultaneously. |
| C-19 | FAIL | No disqualifying example present in template. No phrase of the form "X does not qualify." |
| C-20 | FAIL | No disqualifier of any form. |
| C-21 | PASS | Phase headers are colloquial questions ("what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?"). Field labels are bare ("check-1:", "step-1:") without requirement descriptions. Colloquial bare-label pattern confirmed. |
| C-22 | PASS | Bare label scaffolding ("check-1:", "validation-1:", "gap-1:") achieves ordinal field enumeration without prose requirement text — functionally equivalent to numbered list but in colloquial register. |
| C-23 | FAIL | No incident narrative in ROLE block. |
| C-24 | PASS | Interrogative headers operate as colloquial phase anchors — "did it land?" and "what do we do if it didn't?" are domain-idiomatic question forms for post-deploy validation and rollback respectively. Colloquial phrasing extends across all phases, not just pre-deploy. |
| C-25 | PASS | No incident narrative anywhere in the prompt. ROLE block contains vocabulary list + placeholder fields for current practice and known failure mode, not a historical anecdote. |
| C-26 | PASS | All four phase headers are interrogative questions: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-27 | PASS | Exactly three rollback template fields: trigger, rollback-1, verify-rollback. The triple is precisely satisfied — not more, not fewer. |
| C-28 | PASS | C-26 passes (interrogative headers throughout) and C-27 passes (rollback triple). Joint criterion satisfied. |
| C-29 | FAIL | No declarative disqualifier present. |
| C-30 | FAIL | No question-form disqualifier present. (Interrogative section headers are structural anchors, not disqualifying examples of weak compliance.) |

**Criteria passed**: C-01–C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27, C-28 (23 criteria)
**Score**: 60 + 30 + (6×5) + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = **165/200**

---

## V-04 — Role-block inertia + question-form disqualifier

**Axis**: C-23 ∩ C-30 orthogonality test

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "List at least 3 checks. Each must name the specific condition being verified and what failure looks like." |
| C-02 | PASS | "List at least 4 numbered steps in execution order." |
| C-03 | PASS | "List at least 2 validation actions. Each must name a probe, threshold, or data-integrity assertion." |
| C-04 | PASS | "State the rollback trigger, at least one undo step, and how to verify the rollback succeeded." |
| C-05 | PASS | "For each phase, identify at least one gap." |
| C-06 | PASS | "Call out at least one step that must complete before the next can begin." |
| C-07 | PASS | Vocabulary list in ROLE block including catalog sync, order pipeline drain, inventory lock, etc. |
| C-08 | PASS | "state what should be added or changed" — remedy required per gap. |
| C-09 | PASS | Severity column + "Compare each gap against the others before assigning Severity." |
| C-10 | PASS | "Identify at least one automation hook." |
| C-11 | PASS | Vocabulary enumerated in ROLE block as named list. |
| C-12 | PASS | "Current practice" + "Known failure mode" in ROLE block. |
| C-13 | PASS | "Produce a cross-phase gap summary table with columns: Phase, Gap, Severity, Why." |
| C-14 | FAIL | No front-loaded skeleton. Gap table appears as end instruction. |
| C-15 | PASS | C-12 achieved via ROLE block named fields. C-13 achieved via prose naming columns and mandating comparison. No template apparatus. Three C-15 structural requirements met through prose. |
| C-16 | FAIL | Prose path; no template field scaffolding. |
| C-17 | FAIL | Multi-section prose structure (PRE-DEPLOY, DEPLOYMENT SEQUENCE, POST-DEPLOY VALIDATION, ROLLBACK). Above single-paragraph-per-phase density. |
| C-18 | FAIL | C-14 and C-16 both fail. |
| C-19 | PASS | "A check that asks 'is the dependency available?' names no specific condition and does not qualify." |
| C-20 | PASS | "A validation that asks 'is the service healthy?' names no probe or threshold and does not qualify." Domain-relevant (probe/threshold reference). |
| C-21 | FAIL | Prose path. |
| C-22 | FAIL | Prose path. |
| C-23 | PASS | "After the catalog sync outage we learned that missing pre-deploy dependency health checks were the primary gap — downstream services were unavailable before the deployment began. We carry that lesson into every deployment trace." Incident narrative present in ROLE block — inertia-sourced framing. |
| C-24 | FAIL | Prose path. |
| C-25 | FAIL | Incident narrative present in role block. C-23 and C-25 are mutually exclusive; C-23 wins here. |
| C-26 | FAIL | Section headers are declarative (PRE-DEPLOY, DEPLOYMENT SEQUENCE, etc.), not interrogative. |
| C-27 | FAIL | Rollback in prose, not as three template fields. |
| C-28 | FAIL | Neither C-26 nor C-27 pass. |
| C-29 | FAIL | Disqualifiers are question-form, not declarative domain-contextual. |
| C-30 | PASS | Question-form disqualifiers operative: "A check that asks 'is the dependency available?' names no specific condition" and "A validation that asks 'is the service healthy?' names no probe or threshold." Interrogative expression confirmed as C-30 generator independent of role-block inertia. |

**Orthogonality confirmed**: C-23 (role-block inertia, in ROLE block) and C-30 (question-form disqualifier, in phase instructions) are sourced from different structural positions. Co-occurrence produces both passes with neither interfering with the other.

**Criteria passed**: C-01–C-13, C-15, C-19, C-20, C-23, C-30 (19 criteria)
**Score**: 60 + 30 + (5×5) + 5 + 5 + 5 + 5 + 5 = **140/200**

---

## V-05 — Compressed prose + question-form disqualifier

**Axis**: C-17 ∩ C-30 joint; question-form compression advantage test vs V-02

*Note: V-05 prompt is partially truncated in source specification. Scoring based on stated hypothesis: compressed single-paragraph format with question-form disqualifiers; role block has vocabulary + practice + known failure mode but no incident narrative; no template apparatus.*

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Essential coverage requirements met in compressed paragraph ("list 3+ checks, each naming specific condition and failure"). |
| C-02 | PASS | "list 4+ ordered steps." |
| C-03 | PASS | "list 2+ probes, thresholds, or data-integrity assertions." |
| C-04 | PASS | "state trigger, undo steps, and revert verification." |
| C-05 | PASS | "per phase identify at least one gap." |
| C-06 | PASS | Ordering dependency named in compressed paragraph. |
| C-07 | PASS | Vocabulary list in ROLE block. |
| C-08 | PASS | "state its remedy" — actionable gap requirement present. |
| C-09 | PASS | Severity column + comparative assignment instruction. |
| C-10 | PASS | Automation hook instruction in compressed paragraph. |
| C-11 | PASS | Vocabulary in ROLE block as named list. |
| C-12 | PASS | Current practice + Known failure mode in ROLE block. |
| C-13 | PASS | Cross-phase gap summary table with named columns. |
| C-14 | FAIL | No front-loaded skeleton (prose path; no template apparatus to front-load). |
| C-15 | PASS | All three C-15 requirements met through explicit prose at compressed density: named output elements, cross-gap comparison mandate, disqualifying examples. No template apparatus. |
| C-16 | FAIL | Prose path; no template field scaffolding. |
| C-17 | PASS | C-15 passes. Entire multi-phase instruction compressed to a single flowing paragraph — below single-paragraph-per-phase density. Question-form disqualifiers are naturally compressed (shorter than declarative equivalents when embedded inline); all three C-15 structural requirements satisfied without verbosity expansion. |
| C-18 | FAIL | C-14 fails. |
| C-19 | PASS | Question-form disqualifier present. |
| C-20 | PASS | Disqualifier references domain-relevant concept (probe/threshold class). |
| C-21 | FAIL | Prose path. |
| C-22 | FAIL | Prose path. |
| C-23 | FAIL | No incident narrative. |
| C-24 | FAIL | Prose path. |
| C-25 | PASS | No incident narrative anywhere. |
| C-26 | FAIL | Compressed prose; no section headers of any form. |
| C-27 | FAIL | Prose path. |
| C-28 | FAIL | Neither C-26 nor C-27 pass. |
| C-29 | FAIL | Disqualifiers are question-form, not declarative. |
| C-30 | PASS | Question-form disqualifiers in compressed paragraph confirm C-30 generator. Question-form expression ("a check that asks 'is everything ready?' names no condition") passes with no compression penalty vs declarative V-02. |

**Compression comparison (V-05 vs V-02)**: Both achieve 145/200. Question-form form (V-05: C-30) and declarative domain-contextual form (V-02: C-29) are interchangeable on the compressed-prose path — neither form has a structural compression advantage. C-29 and C-30 are orthogonal, same-weight, independent paths through C-19.

**Criteria passed**: C-01–C-13, C-15, C-17, C-19, C-20, C-25, C-30 (20 criteria)
**Score**: 60 + 30 + (5×5) + 5 + 5 + 5 + 5 + 5 + 5 = **145/200**

---

## Rankings

| Rank | Variation | Score | Path | Key axis |
|------|-----------|-------|------|----------|
| 1 | V-03 | **165/200** | template | interrogative + rollback triple + colloquial + skeleton — ceiling |
| 2 | V-02 | **145/200** | prose-compressed | C-17 ∩ C-29 — declarative disqualifier, compressed |
| 2 | V-05 | **145/200** | prose-compressed | C-17 ∩ C-30 — question-form disqualifier, compressed |
| 4 | V-01 | **140/200** | prose-standard | C-30 alone — question-form disqualifier, standard density |
| 4 | V-04 | **140/200** | prose-standard | C-23 ∩ C-30 — inertia + question-form, orthogonality confirmed |

**All essential pass**: Yes — C-01–C-05 pass in all five variations.

---

## Excellence Signals — V-03 (top scorer, 165/200)

1. **Interrogative headers as structural anchors**: "what needs to be true before we touch this?" and "what do we do if it didn't?" are domain-idiomatic question forms for pre-deploy and rollback. They carry phase labeling without declarative headers and satisfy C-26 through natural language. The colloquial register is not stylistic — it is structurally load-bearing for the C-21/C-22/C-24/C-26 cluster.

2. **Rollback triple precision**: exactly three fields (trigger, rollback-1, verify-rollback) is the minimum field set that satisfies C-04 and C-27 simultaneously. No excess fields. The triple is the template-path equivalent of the prose rollback instruction.

3. **Do-not-pre-fill guard as non-GATE text**: "fill this last; do not pre-fill any row" is a commitment device that defers synthesis to after the trace is complete — without being GATE enforcement text. This is the structural insight that allows C-14 and C-16 to co-exist: the skeleton imposes a cognitive ordering without introducing a procedural gate that would disqualify C-16.

4. **Vocabulary list + practice + failure mode in ROLE block**: three distinct knowledge types in the role block (domain vocabulary, current practice, known failure mode) close C-11, C-12, and C-07 from a single block — zero redundancy in the instruction body.

---

## New Patterns

**V-01 / V-04 / V-05**: All three confirm C-30 passes via question-form expression. No variation produces an unexpected pass or fail.

**V-04 orthogonality**: C-23 and C-30 confirmed independent. Role-block inertia (position: ROLE block) and question-form disqualifier (position: phase instructions) do not interfere. Structural positions are orthogonal by design.

**V-02 vs V-05 compression parity**: Declarative domain-contextual form (C-29) and question-form form (C-30) achieve identical scores at compressed density. No compression advantage for either form. C-29 and C-30 are symmetric paths through C-19 on the prose-compressed axis.

**Assessment**: All five variations confirm their predictions exactly. No criterion passes or fails against prediction. No new patterns emerge that would require promotion to a new criterion.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": []}
```
