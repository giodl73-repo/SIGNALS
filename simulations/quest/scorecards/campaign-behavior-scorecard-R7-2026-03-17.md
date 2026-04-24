# Quest Score — campaign-behavior (org-review) Round 7
**Rubric:** v6 | **Aspirational denominator:** 15 | **Max score:** 90

---

## Scoring Legend

| Symbol | Meaning |
|--------|---------|
| ✅ PASS | Full credit |
| ⚠️ PARTIAL | Half credit |
| ❌ FAIL | 0 |

Aspirational tier: binary PASS/FAIL per criterion; composite = (count passed / 15) × 10, rounded to nearest integer.

---

## Variation Scorecards

### V-01 — State-anchor sequence (single)

**Axis:** Implements optimal execution sequence — trace-state (Ph1) → trace-permissions (Ph2) → trace-contract (Ph3) → flow-lifecycle (Ph4) → flow-trigger (Ph5). Sequence swap delivers both C-22 and C-23 simultaneously.

#### Essential (C-01–C-05)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 All 5 sub-skills executed | ✅ PASS | All five named explicitly in phase sequence |
| C-02 Findings ranked by blast radius | ✅ PASS | Blast radius pre-classification map from Ph1 drives consolidated ranking |
| C-03 Spec gaps identified or cleared | ✅ PASS | Phase outputs surface gaps; explicit "none found" if clean |
| C-04 Contract violations surfaced or cleared | ✅ PASS | Ph3 trace-contract table covers all producer/consumer pairs |
| C-05 (blast radius / severity labeled separately) | ✅ PASS | Ph1 state-anchor enforces structural separation before downstream execution |

**Essential subtotal: 50/50**

#### Recommended (C-06–C-08)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-06 (CONFIRMED / RUNTIME ANOMALY classification) | ✅ PASS | Ph4-5 tables carry CONFIRMED/RUNTIME ANOMALY fields with Ph1-3 match names |
| C-07 (SYSTEMIC flag with phase enumeration) | ✅ PASS | Calibration Q3 enforces phase-name list; binary flags blocked |
| C-08 (Calibration block executed) | ✅ PASS | Q1–Q5 present and answered |

**Recommended subtotal: 30/30**

#### Aspirational (C-09–C-23)

| Criterion | Verdict |
|-----------|---------|
| C-09 through C-21 (inherited from R1–R5) | ✅ PASS ×13 |
| C-22 State-anchor execution order | ✅ PASS — trace-state Ph1 with explicit "state topology pre-classifies blast radius candidates" rationale |
| C-23 Permissions-anchor position | ✅ PASS — trace-permissions Ph2, structurally before flow sub-skills (Ph4, Ph5) |

**Aspirational: 15/15 passed → (15/15) × 10 = 10/10**

**V-01 Total: 50 + 30 + 10 = 90/90**

---

### V-02 — Permissions-anchor rationale reinforcement (single)

**Axis:** Keeps R6 V-04 execution sequence unchanged (trace-permissions at Phase 1, trace-state not first). Adds only explicit "before flow sub-skills" declaration for C-23 isolation test. Diagnostic variation only.

#### Essential (C-01–C-05)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | ✅ PASS | All five sub-skills present |
| C-02 | ✅ PASS | Blast radius ranking present |
| C-03 | ✅ PASS | Spec gaps section present |
| C-04 | ✅ PASS | Contract violations section present |
| C-05 | ✅ PASS | Blast radius / severity labeled separately |

**Essential subtotal: 50/50**

#### Recommended (C-06–C-08)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-06 | ✅ PASS | CONFIRMED / RUNTIME ANOMALY retained from R6 |
| C-07 | ✅ PASS | SYSTEMIC with phase enumeration |
| C-08 | ✅ PASS | Q1–Q5 calibration block |

**Recommended subtotal: 30/30**

#### Aspirational (C-09–C-23)

| Criterion | Verdict |
|-----------|---------|
| C-09 through C-21 (inherited) | ✅ PASS ×13 |
| C-22 State-anchor execution order | ❌ FAIL — trace-state is NOT first; trace-permissions occupies Ph1; no state-topology-pre-classifies rationale present for Ph1 position |
| C-23 Permissions-anchor position | ✅ PASS — explicit "before flow sub-skills" declaration added; trace-permissions at Ph1 is structurally before flow phases regardless |

**Aspirational: 14/15 passed → (14/15) × 10 = 9.33 → 9/10**

**V-02 Total: 50 + 30 + 9 = 89/90**

---

### V-03 — DEPTH asymmetry on state-anchor sequence (single)

**Axis:** Identical optimal sequence to V-01 (trace-state Ph1 → trace-permissions Ph2 → ...) plus explicit DEPTH labels distinguishing structural-anchor phases from execution phases. Targets C-22 + C-23 + depth asymmetry as new aspirational signal.

#### Essential (C-01–C-05)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | ✅ PASS | All five sub-skills in labeled phases |
| C-02 | ✅ PASS | Pre-classified blast radius map drives ranking |
| C-03 | ✅ PASS | Spec gaps section present |
| C-04 | ✅ PASS | Contract violations section present |
| C-05 | ✅ PASS | Blast radius / severity separated at phase level |

**Essential subtotal: 50/50**

#### Recommended (C-06–C-08)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-06 | ✅ PASS | CONFIRMED / RUNTIME ANOMALY in Ph4-5 |
| C-07 | ✅ PASS | SYSTEMIC with corroborating phase names |
| C-08 | ✅ PASS | Full calibration block |

**Recommended subtotal: 30/30**

#### Aspirational (C-09–C-23)

| Criterion | Verdict |
|-----------|---------|
| C-09 through C-21 | ✅ PASS ×13 |
| C-22 | ✅ PASS — trace-state Ph1 with state-topology-pre-classifies rationale; DEPTH label marks Ph1 as structural anchor |
| C-23 | ✅ PASS — trace-permissions Ph2 before flow sub-skills; DEPTH label differentiates anchor phases (Ph1-2) from execution phases (Ph3-5) |

**Aspirational: 15/15 passed → 10/10**

**V-03 Total: 50 + 30 + 10 = 90/90**

> **New pattern candidate:** DEPTH asymmetry labeling — anchor phases (Ph1 state, Ph2 permissions) carry explicit `[ANCHOR]` or `DEPTH: structural` tags distinguishing them from execution phases. Makes the structural dependency chain visible without prose explanation.

---

### V-04 — Dual-anchor + Q6 sequence integrity (combination)

**Axis:** Optimal sequence (C-22 + C-23) plus Q6 — a self-referential calibration question verifying that execution sequence delivered its pre-classification guarantee (zero post-hoc blast radius revisions from sequence order).

#### Essential (C-01–C-05)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | ✅ PASS | All five sub-skills, correct phase order |
| C-02 | ✅ PASS | Blast radius ranking anchored to Ph1 pre-classification |
| C-03 | ✅ PASS | Spec gaps present |
| C-04 | ✅ PASS | Contract violations present |
| C-05 | ✅ PASS | Blast radius / severity labeled separately |

**Essential subtotal: 50/50**

#### Recommended (C-06–C-08)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-06 | ✅ PASS | CONFIRMED / RUNTIME ANOMALY with Ph1-3 match names |
| C-07 | ✅ PASS | SYSTEMIC with phase enumeration |
| C-08 | ✅ PASS | Q1–Q5 + Q6 calibration block (extended) |

**Recommended subtotal: 30/30**

#### Aspirational (C-09–C-23)

| Criterion | Verdict |
|-----------|---------|
| C-09 through C-21 | ✅ PASS ×13 |
| C-22 | ✅ PASS — trace-state Ph1 with structural rationale |
| C-23 | ✅ PASS — trace-permissions Ph2, before flow phases |

**Aspirational: 15/15 passed → 10/10**

**V-04 Total: 50 + 30 + 10 = 90/90**

> **New pattern candidate (structural):** Q6 sequence integrity gate — "Did the execution sequence deliver its pre-classification guarantee? Were any blast radius values revised post-hoc due to sequence order?" This is a self-referential calibration step: if any finding required retroactive blast radius revision after Ph1-2 ran, the anchor claim is violated. Zero revisions = anchor held. Canonical pattern for future rubric versions where execution order is a scored criterion.

---

### V-05 — Full 15-criterion coverage (combination)

**Axis:** Double reinforcement of all C-01–C-23. Every aspirational criterion gets explicit named evidence. Optimal sequence preserved. Maximum redundancy variation.

#### Essential (C-01–C-05)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | ✅ PASS | All five sub-skills with double-named evidence |
| C-02 | ✅ PASS | Blast radius ranking with criterion cited |
| C-03 | ✅ PASS | Spec gaps with labeled section |
| C-04 | ✅ PASS | Contract violations with labeled section |
| C-05 | ✅ PASS | Blast radius / severity separate fields, doubly labeled |

**Essential subtotal: 50/50**

#### Recommended (C-06–C-08)

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-06 | ✅ PASS | CONFIRMED / RUNTIME ANOMALY with dual-phase match citations |
| C-07 | ✅ PASS | SYSTEMIC with phase list, double-stated |
| C-08 | ✅ PASS | Full calibration block, all questions answered verbosely |

**Recommended subtotal: 30/30**

#### Aspirational (C-09–C-23)

| Criterion | Verdict |
|-----------|---------|
| C-09 through C-21 | ✅ PASS ×13 |
| C-22 | ✅ PASS — trace-state Ph1 with explicit anchor declaration AND Q6 verification |
| C-23 | ✅ PASS — trace-permissions Ph2 with explicit "before flow sub-skills" declaration |

**Aspirational: 15/15 passed → 10/10**

**V-05 Total: 50 + 30 + 10 = 90/90**

---

## Composite Rankings

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 (tie) | **V-01** | 50/50 | 30/30 | 10/10 | **90/90** |
| 1 (tie) | **V-03** | 50/50 | 30/30 | 10/10 | **90/90** |
| 1 (tie) | **V-04** | 50/50 | 30/30 | 10/10 | **90/90** |
| 1 (tie) | **V-05** | 50/50 | 30/30 | 10/10 | **90/90** |
| 5 | **V-02** | 50/50 | 30/30 | 9/10 | **89/90** |

---

## Diagnostic Read on V-02

V-02 scores 89/90 rather than 90/90, confirming that **C-22 requires trace-state in Ph1 specifically** — not merely any execution before flow phases. The permissions-anchor rationale alone (explicit "before flow sub-skills" language) earns C-23 regardless of whether permissions sits in Ph1 or Ph2. The two criteria are structurally independent: C-23 is satisfied by position relative to flow phases; C-22 is satisfied only by trace-state holding Ph1. V-02 falsifies the hypothesis that C-23 alone drives the point gap — the single missing point is unambiguously C-22.

---

## Excellence Signals

Two new patterns emerge from the R7 top-scoring variations, eligible for C-24 and C-25:

### Signal 1 — DEPTH asymmetry labeling (from V-03)
Anchor phases (Ph1 state, Ph2 permissions) carry explicit structural markers (e.g., `[ANCHOR: state topology pre-classifies blast radius]`) inline in the phase header. Execution phases (Ph3–Ph5) carry no such label. The asymmetry makes the structural dependency chain immediately visible in the output without requiring prose navigation. Future evaluators can confirm anchor sequencing from headers alone.

### Signal 2 — Q6 sequence integrity gate (from V-04)
A sixth calibration question verifying execution order held its structural guarantee: *"Were any blast radius values revised post-hoc because a finding touched a state surface or escalation role that Ph1 or Ph2 had not yet classified?"* Zero revisions = anchor guarantee delivered. Any revision = anchor was violated and the execution sequence must be re-examined. This is a self-validating check on the core claim of C-22/C-23 — it converts a structural design decision into a runtime-verifiable assertion.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["DEPTH asymmetry labeling — anchor phases carry inline [ANCHOR] markers in phase headers; execution phases carry none; asymmetry makes structural dependency chain visible without prose navigation", "Q6 sequence integrity gate — calibration question verifying zero post-hoc blast radius revisions attributable to execution order; converts C-22/C-23 structural claims into runtime-verifiable assertions"]}
```
