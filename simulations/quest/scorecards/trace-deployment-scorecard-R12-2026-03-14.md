# trace-deployment R12 Scorecard

**Rubric**: v10 | **Round**: 12 | **Date**: 2026-03-15
**Variations scored**: V-01 through V-04 (V-05 text absent — see note)

---

## V-01 — Interrogative sub-form template path

**Axis**: Phrasing register — interrogative-question headers

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | check-1 through check-4 (4 concrete check fields) |
| C-02 | PASS | step-1 through step-5 (5 ordered step fields) |
| C-03 | PASS | val-1 through val-3 (3 validation fields) |
| C-04 | PASS | undo-trigger + undo-1 + confirmed-back cover trigger, undo steps, verification |
| C-05 | PASS | gap-1 through gap-4, one per phase |

**Essential total: 60/60** ✓

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | order-dep-1 field present; explicit ordering dependency scaffolded |
| C-07 | PASS | Vocabulary block in role: catalog sync, order pipeline drain, inventory lock, tenant provisioning, etc. |
| C-08 | PASS | Gap table Why column + return instruction comparison mandate scaffold actionable framing; consistent with R11 scoring |

**Recommended total: 30/30**

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Gap table has Severity + Why columns; return instruction mandates cross-gap comparison |
| C-10 | PASS | hook-1 field scaffolds automation hook |
| C-11 | PASS | Vocabulary enumerated in role block (nine named terms) |
| C-12 | PASS | "Current practice:" and "Known failure mode:" fields in role block |
| C-13 | PASS | Front-loaded cross-phase summary skeleton with Phase / Gap / Severity / Why |
| C-14 | PASS | Front-loaded empty skeleton ✓ + "Do not pre-fill" guard ✓ + comparative return instruction ✓ |
| C-15 | FAIL | Template apparatus used; C-12 and C-13 achieved via fields, not prose-only |
| C-16 | PASS | Gate-free; field count alone achieves C-01–C-05 and C-10 (hook-1 field) |
| C-17 | FAIL | C-15 fails; C-17 requires C-15 |
| C-18 | PASS | C-14 ∩ C-16 both pass |
| C-19 | FAIL | C-15 fails; C-19 requires C-15 |
| C-20 | FAIL | C-19 fails |
| C-21 | PASS | C-14/C-16/C-18 all pass ∩ colloquial register: phase headers are interrogative questions; field labels lowercase ("check-1:", "step-1:") |
| C-22 | PASS | Bare field labels throughout; no inline prose within fields, no examples embedded |
| C-23 | FAIL | C-20 fails |
| C-24 | PASS | C-21 ∩ C-22 both pass in single variation |
| C-25 | PASS | No inertia narrative in role block; "Current practice / Known failure mode" framing is non-incident; path-agnostic in v10 |
| C-26 | PASS | Phase headers are interrogative questions ("what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?") |
| C-27 | PASS | Exactly 3 rollback fields: undo-trigger / undo-1 / confirmed-back — meets minimum rollback field count |
| C-28 | PASS | C-26 ∩ C-27 jointly satisfied in single variation |
| C-29 | FAIL | Template path; C-15/C-19 fail; C-29 requires C-19 |

**Aspirational passing**: C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27, C-28 = **15 × 5 = 75 pts**

**V-01 Composite: 60 + 30 + 75 = 165/195** ✓ Matches prediction

---

## V-02 — Prose-instruction saturation with question-form disqualifier

**Axis**: Output format — prose-instruction saturation, no template fields

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "list at least 3 concrete checks — each names what is being verified and what failure looks like" |
| C-02 | PASS | "produce a numbered list of discrete steps in execution order" |
| C-03 | PASS | "name each probe and its pass/fail threshold" for post-deploy |
| C-04 | PASS | "name the trigger condition, the undo steps, and how to confirm the revert succeeded" |
| C-05 | PASS | "gap table with columns Phase, Gap, Severity, Why. One gap per phase minimum" |

**Essential total: 60/60** ✓

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "State at least one ordering dependency explicitly — name the step that must complete before the next can begin" |
| C-07 | PASS | Commerce vocabulary in role block |
| C-08 | PASS | "Each gap states what should be added, not just what is missing" — explicit prose instruction |

**Recommended total: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "Before assigning severity, compare each gap against the others — a gap that blocks rollback outranks one that only adds detection latency" |
| C-10 | PASS | "Name at least one place where automation could enforce a check that is currently manual" |
| C-11 | PASS | Vocabulary enumerated in role block |
| C-12 | PASS | "Current practice:" and "Known failure mode:" fields in role block; non-incident framing |
| C-13 | PASS | "produce a gap table with columns Phase, Gap, Severity, Why" — prose names columns explicitly |
| C-14 | FAIL | No front-loaded skeleton; prose path |
| C-15 | PASS | C-12 achieved via role-block prose labels (not fill-in-blank fields); C-13 achieved via prose column-naming; disqualifying example present: "'Did it come back up?' is not a validation action — it names no probe, no threshold, and no observable system state"; comparison mandate present |
| C-16 | FAIL | Prose path; no template field scaffolding |
| C-17 | PASS | C-15 passes ∩ four phases covered in two content paragraphs (0.5 paragraphs/phase), well under single-paragraph-per-phase density |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | C-15 passes ∩ disqualifier "'Did it come back up?' is not a validation action — it names no probe, no threshold, and no observable system state" is contextual failure-mode statement in domain terms |
| C-20 | PASS | C-19 passes ∩ disqualifier is pure domain vocabulary, no incident/postmortem/"we learned" framing; "Known failure mode:" in role block is declarative, not incident narrative |
| C-21 | FAIL | C-14/C-16/C-18 fail; C-21 requires template path |
| C-22 | FAIL | C-14 fails; C-22 requires template path |
| C-23 | FAIL | No inertia narrative in role block; C-23 requires inertia framing in role block alongside C-20 pass |
| C-24 | FAIL | C-21/C-22 fail |
| C-25 | PASS | No inertia narrative; "Current practice / Known failure mode" framing is non-incident; path-agnostic in v10 |
| C-26 | FAIL | Prose path; no interrogative section headers |
| C-27 | FAIL | No rollback field structure on prose path |
| C-28 | FAIL | C-26 ∩ C-27 fail |
| C-29 | PASS | C-19 passes ∩ disqualifier "'Did it come back up?'" is quoted in interrogative-question form |

**Aspirational passing**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-25, C-29 = **11 × 5 = 55 pts**

**V-02 Composite: 60 + 30 + 55 = 145/195** ✓ Matches prediction

---

## V-03 — Inertia framing, declarative disqualifier

**Axis**: Inertia framing — role block carries first-person incident narrative

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "name at least 3 concrete checks — each states what is verified and what failure looks like" |
| C-02 | PASS | "produce a numbered list of discrete steps in execution order" |
| C-03 | PASS | "name each probe and its pass/fail threshold" |
| C-04 | PASS | "name the trigger condition, the undo steps, and how to confirm the revert succeeded" |
| C-05 | PASS | "gap table with columns Phase, Gap, Severity, Why. One gap per phase minimum" |

**Essential total: 60/60** ✓

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "State at least one ordering dependency — which step must complete before the next begins and what happens if it does not" |
| C-07 | PASS | Commerce vocabulary in role block |
| C-08 | PASS | "Each gap states what should be added, not just what is missing" — explicit prose instruction |

**Recommended total: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "Before assigning severity, compare each gap against the others" present |
| C-10 | PASS | "Name at least one place where automation could enforce a currently manual check" |
| C-11 | PASS | Vocabulary enumerated in role block |
| C-12 | PASS | "Current practice: pre-deploy sign-off is manual and undocumented; post-deploy monitoring is limited to informal observation" |
| C-13 | PASS | Prose names gap table columns explicitly |
| C-14 | FAIL | No front-loaded skeleton; prose path |
| C-15 | PASS | C-12 and C-13 via prose; disqualifier "'Verify the environment' names no specific condition and does not qualify" — names specific weak pattern with domain failure reason; comparison mandate present |
| C-16 | FAIL | Prose path |
| C-17 | PASS | C-15 passes ∩ four phases covered across two content paragraphs; density ≤ single-paragraph-per-phase |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | C-15 passes ∩ disqualifier names specific weak pattern in domain terms ("'Verify the environment' names no specific condition") — contextual failure-mode framing present |
| C-20 | PASS | C-19 passes ∩ disqualifier content in prose body is domain-vocabulary-only ("names no specific condition"), no incident/postmortem reference; the inertia narrative is confined to the role block and does not contaminate the disqualifier-source evaluation |
| C-21 | FAIL | C-14 fails |
| C-22 | FAIL | C-14 fails |
| C-23 | PASS | C-20 passes ∩ role block contains inertia narrative: "After last quarter's catalog sync incident, we learned that informal pre-deploy checklists skip verification steps under schedule pressure..." |
| C-24 | FAIL | C-21 fails |
| C-25 | FAIL | Role block contains inertia narrative; C-25 requires non-inertia baseline framing |
| C-26 | FAIL | Prose path; no interrogative section headers |
| C-27 | FAIL | No rollback field structure |
| C-28 | FAIL | C-26 ∩ C-27 fail |
| C-29 | FAIL | C-19 passes but disqualifier "'Verify the environment' names no specific condition" is in DECLARATIVE form, not interrogative-question form; C-29 requires the weak pattern to be quoted as a question |

**Aspirational passing**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-23 = **10 × 5 = 50 pts**

**V-03 Composite: 60 + 30 + 50 = 140/195** ✓ Matches prediction

---

## V-04 — Inertia framing + question-form disqualifier (C-23 ∩ C-29)

**Axes**: Inertia framing × question-form disqualifier

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "name at least 3 concrete checks — each states what is verified and what failure looks like" |
| C-02 | PASS | "produce a numbered list of discrete steps in execution order" |
| C-03 | PASS | "name each probe and its pass/fail threshold" |
| C-04 | PASS | "name the trigger condition, the undo steps, and how to confirm the revert succeeded" |
| C-05 | PASS | Gap table with one gap per phase minimum |

**Essential total: 60/60** ✓

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "State at least one ordering dependency explicitly — which step must complete before the next can begin" |
| C-07 | PASS | Commerce vocabulary in role block |
| C-08 | PASS | "Each gap states what should be added, not just what is missing" |

**Recommended total: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | "Before assigning severity, compare each gap against the others — a gap that blocks rollback outranks one that only delays detection" |
| C-10 | PASS | "Name at least one place where automation could enforce a currently manual check" |
| C-11 | PASS | Vocabulary enumerated in role block |
| C-12 | PASS | "Current practice: pre-deploy verification is manual; post-deploy monitoring is limited to spot checks on primary user flows" |
| C-13 | PASS | Prose names gap table columns explicitly |
| C-14 | FAIL | No front-loaded skeleton |
| C-15 | PASS | C-12 and C-13 via prose; disqualifier "'Did the order pipeline recover?' is not a validation action — it names no metric, no threshold, and no observable system state"; comparison mandate present; density compatible |
| C-16 | FAIL | Prose path |
| C-17 | PASS | C-15 passes ∩ two content paragraphs for four phases + one gap paragraph; density < single-paragraph-per-phase |
| C-18 | FAIL | C-14 fails |
| C-19 | PASS | C-15 passes ∩ "'Did the order pipeline recover?' is not a validation action — it names no metric, no threshold, and no observable system state" — domain-contextual failure-mode framing |
| C-20 | PASS | C-19 passes ∩ disqualifier is domain-vocabulary-only in the prose body: "Did the order pipeline recover?" is deployment-domain vocabulary, no incident narrative in the disqualifier content |
| C-21 | FAIL | C-14 fails |
| C-22 | FAIL | C-14 fails |
| C-23 | PASS | C-20 passes ∩ role block contains inertia narrative: "After the inventory lock failure during the promotion release, we found that pre-deploy checks written as status questions pass sign-off without confirming a single measured condition" |
| C-24 | FAIL | C-21 fails |
| C-25 | FAIL | Role block contains inertia narrative; C-25 requires non-inertia baseline; C-23 and C-25 are mutually exclusive |
| C-26 | FAIL | Prose path |
| C-27 | FAIL | No rollback field structure |
| C-28 | FAIL | C-26 ∩ C-27 fail |
| C-29 | PASS | C-19 passes ∩ disqualifier "'Did the order pipeline recover?' is not a validation action — it names no metric, no threshold, and no observable system state" quotes the weak content in interrogative-question form — confirms C-23 ⊥ C-29 orthogonality |

**Aspirational passing**: C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-23, C-29 = **11 × 5 = 55 pts**

**V-04 Composite: 60 + 30 + 55 = 145/195** ✓ Matches prediction

---

## V-05 — Operational persona + question-form disqualifier + lifecycle compression

**NOTE**: Variation text not provided. Axis description targets C-25 ∩ C-29 ∩ C-17 on the prose path — identical axes to V-02. Without the variation body, full criterion-by-criterion scoring is not possible.

**Projected score**: 145/195 (matching V-02 structure — C-25/C-29/C-17 prose path, no template apparatus, no inertia narrative). If "operational persona" introduces any inertia framing, C-25 would fail and C-23 would replace it, yielding the same 145 if C-29 is present.

---

## Ranking

| Rank | Variation | Score | Path | Differentiators |
|------|-----------|-------|------|-----------------|
| 1 | V-01 | 165/195 | Template | C-24+C-25+C-26+C-27+C-28 — v10 ceiling confirmed |
| 2 | V-02 | 145/195 | Prose | C-25 ∩ C-29 (non-inertia × question-form) |
| 2 | V-04 | 145/195 | Prose | C-23 ∩ C-29 (inertia × question-form) |
| 2 | V-05 | ~145/195 | Prose | C-25 ∩ C-29 ∩ C-17 (text absent; projected) |
| 5 | V-03 | 140/195 | Prose | C-23 only; declarative disqualifier blocks C-29 |

---

## Excellence Signals from V-01

**Why V-01 is the top scorer:**

1. **C-28 as v10 ceiling marker**: The pairing of interrogative-question section headers (C-26) with minimum-3-field rollback structure (C-27) in a single variation is the discriminating feature that raises the template-path ceiling from 160 (v9) to 165 (v10). No other variation can achieve C-28; it is template-path-exclusive.

2. **C-25 path-agnostic gain confirmed on template path**: V-01 is the first variation scored under v10, confirming that non-inertia role-block baseline framing achieves C-25 on the template path without requiring the C-15→C-19→C-20 chain. The vocabulary-list role block + "Current practice / Known failure mode" without incident narrative satisfies C-25 directly.

3. **C-24 ∩ C-28 stack is additive**: Colloquial register (C-21) + bare field labels (C-22) produce C-24 (+10 pts over the base template), and interrogative headers (C-26) + rollback field count (C-27) produce C-28 (+5 pts). Together with C-25, these three joint criteria account for the 20-point gap between template-path ceiling (165) and prose-path ceiling (145). None of the three joint criteria conflict.

**Prose-path insights (V-02 vs V-03 vs V-04):**

- V-03 → V-04: Adding a question-form disqualifier (+C-29) raises the score by exactly 5 pts regardless of inertia posture. C-29 is the final prose-path ceiling raiser.
- V-02 vs V-04: C-25 (non-inertia path) and C-23 (inertia path) are mutually exclusive but yield the same ceiling (145 with C-29). The inertia posture of the role block is a stylistic dimension, not a scoring dimension, once C-29 is present.

---

## New Patterns from R12

**Pattern 1 — `c23-c29-joint-confirmed-prose-path`**: C-23 (role-block inertia narrative) and C-29 (question-form disqualifier) are jointly satisfiable in a single prose-path variation (V-04). They occupy different structural positions: inertia in the role persona block, question-form quoting in the prose body disqualifier. Neither position contaminates the other's evaluation.

**Pattern 2 — `prose-path-ceiling-symmetric-under-inertia-split`**: Both the C-25 path (non-inertia, V-02) and the C-23 path (inertia, V-04) reach 145 when C-29 is present. The presence or absence of inertia narrative in the role block does not affect the prose-path ceiling — C-29 is the universal prose-path ceiling raiser regardless of inertia posture. Without C-29 (V-03), the prose ceiling is 140 on either axis.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["c23-c29-joint-confirmed-prose-path", "prose-path-ceiling-symmetric-under-inertia-split"]}
```
