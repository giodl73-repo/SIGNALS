# trace-deployment — Round 8 Scorecard

**Rubric**: v7 | **Total possible**: 170 pts | **Variations scored**: V-01 through V-04 (V-05 not present in input)

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05) — 60 pts

All four variations pass all five essential criteria. Each prompt explicitly floors count requirements and disqualifies weak compliance.

| ID | V-01 | V-02 | V-03 | V-04 | Notes |
|----|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | ≥3 named checks with failure-condition requirement in all four |
| C-02 | PASS | PASS | PASS | PASS | ≥4 numbered steps required explicitly |
| C-03 | PASS | PASS | PASS | PASS | ≥2 specific validations; "'keep an eye on error rates' does not pass" disqualifier closes weak compliance |
| C-04 | PASS | PASS | PASS | PASS | Trigger + steps + verification all required |
| C-05 | PASS | PASS | PASS | PASS | One gap per phase required; gap-pre/gap-sequence/gap-validation/gap-rollback in V-03; prose instruction in V-01/V-02; field architecture in V-04 |

**Essential subtotal**: 60/60 for all variations.

---

### Recommended Criteria (C-06–C-08) — 30 pts

| ID | V-01 | V-02 | V-03 | V-04 | Notes |
|----|------|------|------|------|-------|
| C-06 | PASS | PASS | PASS | PASS | V-01/V-02: "call out at least one explicit ordering dependency"; V-03: `must-happen-first:` field; V-04: ordering dependency field in template |
| C-07 | PASS | PASS | PASS | PASS | All four carry vocabulary lists in role block with Commerce/Operations terms |
| C-08 | PASS | PASS | PASS | PASS | V-01/V-02: "state what should be added or changed — not just that something is missing"; V-03: illustrated field content "[what's missing… and what to add]"; V-04: return instruction closes this |

**Recommended subtotal**: 30/30 for all variations.

---

### Aspirational Criteria (C-09–C-24) — 80 pts (5 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 |
|----|-----------|------|------|------|------|
| C-09 | Gaps prioritized by risk | PASS | PASS | PASS | PASS |
| C-10 | Automation hook identified | PASS | PASS | PASS | PASS |
| C-11 | Vocabulary list in role block | PASS | PASS | PASS | PASS |
| C-12 | Status-quo baseline before gap analysis | PASS | PASS | PASS | PASS |
| C-13 | Cross-phase gap summary table | PASS | PASS | PASS | PASS |
| C-14 | Front-loaded skeleton + comparative return instruction | **FAIL** | **FAIL** | PASS | PASS |
| C-15 | Prose-instruction saturation closes structural criteria | PASS | PASS | **FAIL** | **FAIL** |
| C-16 | Gate-free essential coverage via template field scaffolding | **FAIL** | **FAIL** | PASS | PASS |
| C-17 | C-15 at minimum prose density | PASS | PASS | **FAIL** | **FAIL** |
| C-18 | C-14 and C-16 simultaneously | **FAIL** | **FAIL** | PASS | PASS |
| C-19 | C-15 disqualifier by contextual failure-mode framing | PASS | PASS | **FAIL** | **FAIL** |
| C-20 | C-19 without inertia narrative source | PASS | PASS | **FAIL** | **FAIL** |
| C-21 | Template path, colloquial register | **FAIL** | **FAIL** | PASS | **FAIL** |
| C-22 | Template path, bare field labels | **FAIL** | **FAIL** | **FAIL** | PASS |
| C-23 | Role-block inertia orthogonal to C-20 disqualifier source | **FAIL** | PASS | **FAIL** | **FAIL** |
| C-24 | C-21 and C-22 jointly satisfied | **FAIL** | **FAIL** | **FAIL** | **FAIL** |

#### C-14 rationale (V-01, V-02 FAIL)
Both prose variations place the gap table instruction at the end of the prompt ("Produce a cross-phase gap table…"). C-14 requires the table to appear as an empty skeleton *before* Phase 1. Prose path does not include template apparatus — no front-loaded skeleton is present.

#### C-16 rationale (V-01, V-02 FAIL)
Prose path has no template field count architecture. Field-count-floors requirement (≥3 Check-NN, ≥4 Step-NN, ≥2 Validation-NN, etc.) requires structural scaffolding, not prose instructions. Prose instructions mandate counts but are not template field scaffolding.

#### C-15 rationale (V-03, V-04 FAIL)
Both template variations achieve structural criteria through field scaffolding, not prose-instruction saturation. The criterion explicitly requires "without structural template apparatus." Template fields, section headers, and skeleton structure disqualify C-15.

#### C-19/C-20 rationale (V-03, V-04 FAIL)
C-19 requires C-15 to pass first. Template path fails C-15 → C-19 and C-20 are unreachable on the template path.

#### C-21 rationale (V-04 FAIL)
V-04 uses formal labels ("## PHASE 1 — PRE-DEPLOY", "Check-NN:", "Step-NN:"). C-21 requires colloquial labels. V-04 is the bare-formal-labels variation — formal register is the explicit design choice.

#### C-22 rationale (V-03 FAIL)
V-03 carries inline field illustrations: `check-1: [name what you're confirming and what failure looks like]`, `validate-1: [specific probe, threshold, or assertion — not 'look for errors']`. C-22 requires no inline prose within fields. Illustrative content inside field definitions disqualifies.

#### C-23 rationale (V-02 PASS, V-01 FAIL)
V-02 role block: "After a catalog sync outage we learned that our post-deploy health checks existed in the documentation but were not wired to any monitoring threshold…. After a tenant provisioning rollback we found we had never written down the rollback verification step." This is explicit first-person incident framing. V-02's disqualifier ("'Keep an eye on error rates' does not name a probe or threshold") is domain-vocabulary-only with no incident reference — C-20 evaluation is of the disqualifier position only, not the role persona. The two positions are structurally independent. C-23 PASS.

V-01 role block contains no incident narrative ("Current practice: deployments run from a shared manual checklist. Known failure mode: pre-deploy checks pass on paper…"). This is present-tense operational description, not inertia narrative. C-23 requires first-person "we learned / we found" incident framing in the persona. FAIL.

#### C-24 rationale (all FAIL)
C-24 requires C-21 and C-22 jointly in a single variation. V-03 satisfies C-21 (colloquial) but fails C-22 (illustrated fields). V-04 satisfies C-22 (bare labels) but fails C-21 (formal register). No variation combines both. This is the missing test — the V-05 gap.

---

## Aspirational Subtotals

| Variation | Passing aspirational criteria | Pts |
|-----------|-------------------------------|-----|
| V-01 | C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20 | 45 |
| V-02 | C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, **C-23** | 50 |
| V-03 | C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21 | 45 |
| V-04 | C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-22 | 45 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 60 | 30 | 45 | **135/170** | YES |
| V-02 | 60 | 30 | 50 | **140/170** | YES |
| V-03 | 60 | 30 | 45 | **135/170** | YES |
| V-04 | 60 | 30 | 45 | **135/170** | YES |

**Ranking**: V-02 > V-01 = V-03 = V-04

All variations pass the golden threshold (all essential pass + composite ≥ 80).

---

## Excellence Signals

**Top variation: V-02 at 140/170**

The distinguishing property: V-02 adds inertia narrative to the role persona while keeping the disqualifier in deployment-domain vocabulary only. The inertia content occupies the role/persona structural position; the disqualifier content occupies the gap-analysis instruction position. These are fully independent dimensions — C-23 evaluates role-block content; C-20 evaluates disqualifier-source content. Adding inertia to the persona does not contaminate the C-20 evaluation and costs nothing on any other criterion.

**Template path ceiling confirmed at 135 for single-axis variations**: V-03 (C-21 only) and V-04 (C-22 only) both score 135. The template path cannot reach 150 until C-21 and C-22 are jointly satisfied (C-24). That joint test is absent — V-05 is the gap.

**Prose path + C-23 (140) outperforms single-axis template (135)**: The prose path with role-block inertia reaches a higher ceiling than either colloquial-only or bare-labels-only template variations. This will invert when template path achieves C-24.

---

## Missing Test: V-05 Gap

C-24 requires a single variation that passes both C-21 (colloquial register) and C-22 (bare field labels). That combination — colloquial headers with bare identifiers and no inline illustration — would add 10 pts to the C-14/C-16/C-18 base and push the template path ceiling to 150/170. No such variation was included in R8. This is the primary open axis for R9.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["prose-path-c23-ceiling-140-outperforms-single-axis-template-135", "c24-joint-test-missing-v05-gap-for-r9"]}
```
