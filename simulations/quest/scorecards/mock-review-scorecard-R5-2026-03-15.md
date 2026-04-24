## /quest:score — mock-review Round 5

**Rubric:** v5 | **Variations:** V-01 through V-05 | **Criteria:** C-01 through C-21

---

## Baseline Inheritance from R4 V-05

All five variations carry forward R4 V-05's ceiling, which already earned full Essential, full Recommended, and C-09 through C-19 in Aspirational. The only two open criteria entering R5 are **C-20** (contrastive MOCK-ACCEPTED rationale) and **C-21** (SQ answer structural signal). Each variation is scored against the full 21-criterion set; the key differentiator is which gap(s) each axis closes.

---

## Criterion-by-Criterion Scoring

### Essential Criteria — all variations

| Criterion | All 5 Variations | Evidence |
|-----------|-----------------|---------|
| C-01 Decision completeness | PASS | STEP 1 extracts all fields; STEP 2 gate: "every namespace placed in exactly one list" before STEP 3 |
| C-02 Auto-rule correctness | PASS | Rules fire in STEP 2 before any evaluation step; three explicit DO NOT marks; STOP gate before STEP 3 |
| C-03 MOCK-ACCEPTED reason codes | PASS | Exact codes in template; "exact codes only; NEVER invent codes" |
| C-04 Status write-back | PASS | STEP 8 labeled mandatory, non-skippable; Edit tool specified; in-place replacement only |
| C-05 Next-steps priority order | PASS | Pre-printed skeleton with explicit "Critical first, evidence-heavy last" rule; three labeled priority buckets |

**Essential: 5/5 for all variations → 60 pts each.**

---

### Recommended Criteria — all variations

| Criterion | All 5 Variations | Evidence |
|-----------|-----------------|---------|
| C-06 Rule trigger named | PASS | `trigger = {rule}` field in every decision block; canonical notation in STEP 6 |
| C-07 PM/Arch/Strategy shown | PASS | All three roles evaluated with separate steps and sub-questions for all non-auto namespaces |
| C-08 Tier flag respected | PASS | Tier read and sourced in STEP 1; TIER-CRITICAL rule gates on `tier >= 2`; tier variable threads throughout |

**Recommended: 3/3 for all variations → 30 pts each.**

---

### Aspirational Criteria — by variation

#### Shared baseline (C-09 through C-19 — inherited from R4 V-05)

| Criterion | Status | Evidence note |
|-----------|--------|--------------|
| C-09 Coverage gap synthesis | PASS | Mandatory cross-namespace risk statement with urgency grouping (BLOCKING / HIGH / MEDIUM); pre-printed skeleton forces all four sections |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | PASS | Rationale slot is namespace-specific in all variations (V-02/V-05 add two-slot structure that makes it richer still) |
| C-11 Forbidden-output enumeration | PASS | All three rules carry explicit DO NOT sentences naming the prohibited output per rule |
| C-12 Zero-remaining confirmation gate | PASS | STEP 8 canary gate; verification before confirming required |
| C-13 Verifiable role-step separation | PASS | PM, Architect, Strategy each have own numbered STEP heading, three sub-questions, and named verdict |
| C-14 SQ citation in verdict | PASS | Citation slot (or Artifact state field) present and linked to specific SQ answer in all variations |
| C-15 Entity-naming SQ grammar | PASS | All sub-questions use "Name X" or "What specific X" form; "not a yes/no judgment" stated |
| C-16 Canary as canary (prohibited under failure) | PASS | CANARY-FALSE-POSITIVE named; suppression path: "CANARY SUPPRESSED: {N} field(s) not updated — {list}" |
| C-17 Contamination guard with named error | PASS | "auto-rule contamination" named; detection rule: "auto-flagged namespace that carries both trigger label AND evaluation verdict" |
| C-18 Inter-step gate with forward reference | PASS | Every gate: "DO NOT proceed to STEP N+1 until..." — names the blocked step by number |
| C-19 Structured trigger notation | PASS | `trigger = {value}` in fixed field position; "free-form text mentioning the rule name outside this field position does not satisfy" |

These 11 criteria are PASS across all five variations.

---

#### C-20 and C-21 — variation-by-variation

**V-01 (Strategy-first):**

| C-20 | PARTIAL | Rationale slot says "drawing on the Strategy SQ-1 answer... the Tier decision this namespace supports should inform why structural coverage is sufficient" — references tier decision but no structural slot forces the contrast. Confirmatory sentence can still satisfy: "supports the go/no-go decision; structural coverage is sufficient for that decision." Framing helps; no guarantee. |
| C-21 | FAIL | REAL-REQUIRED template: "not a restatement of the verdict" prohibition only. No positive present-tense form; verdict echo error unnamed. |

**V-02 (Contrastive rationale template):**

| C-20 | PASS | Two-slot template: `Structural position` names the specific property; `Contrast` requires naming an external namespace type AND structural factor — a confirmatory sentence cannot satisfy the Contrast slot because the slot grammar requires an external comparison. Confirmatory echo error named in template ("A Contrast field that says 'unlike evidence-heavy namespaces, this is structural' names a category but not a structural factor. Named error."). |
| C-21 | FAIL | REAL-REQUIRED template unchanged from R4 V-05: "not a restatement of the verdict" only. No Artifact state field; no present-tense form specified; verdict echo unnamed. |

**V-03 (Present-tense artifact grammar):**

| C-20 | FAIL | MOCK-ACCEPTED template unchanged from R4 V-05: "One sentence: why this code applies to this specific namespace." No two-slot structure; no contrastive requirement. Confirmatory sentence satisfies. |
| C-21 | PASS | `Artifact state` field replaces SQ citation slot. Grammar fully specified: artifact is grammatical subject, verb present tense, observable state is object. Three correct forms shown. Verdict echo named as detectable error: "grammatical subject is a role name or evaluation noun... detectable by grammatical subject inspection." Three echo examples shown with explanation of why each fails. |

**V-04 (Role sequence + inertia framing):**

| C-20 | PARTIAL | DEFAULT DECISION POSITION block makes MOCK-ACCEPTED an earned escape. Rationale says "name what this namespace has (or lacks) compared to namespaces that remain REAL-REQUIRED." This is the most explicitly contrastive instruction yet, but no structural slot forces the comparison. Escape framing aids; two-slot template required for guarantee. |
| C-21 | FAIL | REAL-REQUIRED template unchanged: "not a restatement of the verdict" prohibition only. Inertia framing does not affect citation slot grammar. |

**V-05 (Ceiling — contrastive template + present-tense grammar + inertia framing):**

| C-20 | PASS | V-02 two-slot template carried forward and enhanced: `Structural position` now explicitly references Strategy SQ-1 ("The tier decision this namespace supports (from Strategy SQ-1) should appear here: a namespace supporting a structural-form decision does not need tier-boundary validation"). `Contrast` requires naming namespace type AND structural factor with example. Confirmatory echo error named for both slots. Inertia framing motivates why the escape argument is inherently contrastive — MOCK-ACCEPTED must argue against the REAL-REQUIRED default. |
| C-21 | PASS | V-03 Artifact state grammar carried forward and enhanced: full grammar specification with correct-form examples, verdict echo named with three examples and grammatical detection rule ("subject is a role name or evaluation noun rather than an artifact name"). The Artifact state field also propagates into next-steps entry format: "/{skill-id} {topic} — {artifact state from Artifact state field if eval-driven}" — end-to-end traceability. |

---

## Full Scoring Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Decision completeness | P | P | P | P | P |
| C-02 Auto-rule correctness | P | P | P | P | P |
| C-03 MOCK-ACCEPTED codes | P | P | P | P | P |
| C-04 Status write-back | P | P | P | P | P |
| C-05 Next-steps order | P | P | P | P | P |
| C-06 Trigger named | P | P | P | P | P |
| C-07 All three roles | P | P | P | P | P |
| C-08 Tier flag | P | P | P | P | P |
| C-09 Gap synthesis | P | P | P | P | P |
| C-10 NS-specific rationale | P | P | P | P | P |
| C-11 Forbidden-output enum | P | P | P | P | P |
| C-12 Zero-remaining gate | P | P | P | P | P |
| C-13 Role-step separation | P | P | P | P | P |
| C-14 SQ citation | P | P | P | P | P |
| C-15 Entity-naming SQ grammar | P | P | P | P | P |
| C-16 Canary (prohibited under failure) | P | P | P | P | P |
| C-17 Contamination guard | P | P | P | P | P |
| C-18 Gate with forward ref | P | P | P | P | P |
| C-19 Structured trigger notation | P | P | P | P | P |
| **C-20 Contrastive rationale** | **Pt** | **P** | **F** | **Pt** | **P** |
| **C-21 SQ structural signal** | **F** | **F** | **P** | **F** | **P** |
| Essential pass | 5 | 5 | 5 | 5 | 5 |
| Recommended pass | 3 | 3 | 3 | 3 | 3 |
| Aspirational pass | 11.5 | 12 | 12 | 11.5 | 13 |

*P = PASS, Pt = PARTIAL (0.5), F = FAIL*

---

## Composite Scores

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/13 × 10)`

| V | Essential | Recommended | Aspirational | **Total** |
|---|-----------|-------------|--------------|-----------|
| V-01 | 60.0 | 30.0 | 11.5/13 × 10 = 8.85 | **98.85** |
| V-02 | 60.0 | 30.0 | 12/13 × 10 = 9.23 | **99.23** |
| V-03 | 60.0 | 30.0 | 12/13 × 10 = 9.23 | **99.23** |
| V-04 | 60.0 | 30.0 | 11.5/13 × 10 = 8.85 | **98.85** |
| **V-05** | **60.0** | **30.0** | **13/13 × 10 = 10.00** | **100.00** |

**Ranking:** V-05 > V-02 = V-03 > V-01 = V-04

---

## Excellence Signals from V-05

**What made V-05 the ceiling:**

1. **Inertia framing makes contrastive rationale semantically motivated, not just structurally forced.** The DEFAULT DECISION POSITION block reframes the entire skill: MOCK-ACCEPTED is an earned escape from default, not a symmetric outcome. This means the two-slot template's Contrast field isn't an arbitrary structural requirement — it answers the question the inertia framing already raised ("what distinguishes this namespace from those that remain REAL-REQUIRED?"). The template and the framing are semantically coherent.

2. **Two-slot MOCK-ACCEPTED template makes confirmatory echo structurally unsatisfiable.** `Structural position` can be satisfied with a confirmatory sentence ("no tier-gating decisions"), but `Contrast` cannot — the slot grammar requires naming an external namespace type AND the structural factor it has. A model cannot write "unlike evidence-heavy namespaces, this is structural" because the slot requires the structural factor. The echo error is also named, so failure is diagnosable.

3. **Present-tense artifact grammar converts C-21 from prohibition to positive rule.** "Not a restatement" tells the model what to avoid; "artifact as grammatical subject, present tense verb, observable state as object" tells the model what to produce. The verdict echo error is named with a grammatical detection pattern (role/evaluation as subject), making errors detectable by structural inspection rather than judgment.

4. **Artifact state propagates end-to-end: decision block → next-steps entry format.** The next-steps format for evaluation-driven REAL-REQUIRED entries uses "{artifact state from Artifact state field}" — not a free-form reason, but a field reference. This propagates the present-tense artifact citation from the decision block into the action item, ensuring the review artifact's action items are traceable to the same observable artifact layer as the decisions that produced them.

**New patterns visible in V-05 not yet captured in C-01 through C-21:**

**Pattern A — Cross-step citation linkage:** The `Structural position` slot explicitly references Strategy SQ-1 by step number and sub-question ID: "The tier decision this namespace supports (from Strategy SQ-1) should appear here." This creates a cross-step coherence constraint: the MOCK-ACCEPTED rationale is grounded in a specific named prior evaluation output, making it verifiable against that output. No current criterion requires citation slots to reference specific prior-step outputs by step and SQ number. A rationale that contradicts the SQ-1 answer is now detectable.

**Pattern B — Artifact state propagation into next-steps:** The next-steps entry format for evaluation-driven entries uses the Artifact state field citation by field name ("artifact state from Artifact state field if eval-driven"), not a free-form description. This ensures end-to-end traceability: the same present-tense artifact observation that drove the REAL-REQUIRED decision appears in the action item that follows from it. No current criterion requires citation fields in decision blocks to propagate into next-steps entry format by field reference.

---

## Scorecard File

**Saved to:** `simulations/quest/golden/mock-review-variate-R5-2026-03-15.md`
(scoring table populated inline above)

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Cross-step citation linkage: MOCK-ACCEPTED rationale slot references a specific prior-step evaluation output (Strategy SQ-1) by step number and sub-question ID, making the rationale verifiable against the evaluation that produced it — no current criterion requires citation slots to ground rationale in named prior-step outputs", "Artifact state propagation into next-steps: evaluation-driven REAL-REQUIRED next-steps entries reference the decision block's Artifact state field by field name rather than free-form description, propagating the present-tense artifact citation end-to-end from decision to action item — no current criterion requires citation fields to propagate into next-steps entry format by field reference"]}
```
