## /quest:score — mock-review Round 6

### Rubric Version: v6 | Aspirational Denominator: 16

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/16 × 10)`

PARTIAL = 0.5 credit. PASS = 1.0. FAIL = 0.

---

## V-01 — Inertia Framing Isolation

**Axis:** inertia-framing | DEFAULT DECISION POSITION block, PM-first, single Rationale slot

### Essential

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Two-list separation (auto-flagged + remaining). STOP gate before proceeding. All namespaces placed exactly once. |
| C-02 Automatic rule correctness | P | Three rules with forbidden-output language ("DO NOT mark any EVIDENCE-HEAVY...regardless of..."). Hard STOP between auto-flag and evaluation phases. |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes only; "no paraphrase; NEVER invent codes" present. |
| C-04 Status write-back | P | STEP 8 "mandatory, non-skippable"; Edit tool; in-place replacement only; verification before confirming. |
| C-05 Next-steps priority order | P | "Critical first, evidence-heavy last" ordering rule stated explicitly; four-section skeleton with Priority 1/2/3 + cross-namespace risk statement. |

**Essential: 5/5 → 60 pts**

### Recommended

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-06 Rule trigger named | P | Canonical `trigger = {value}` field in all decision blocks; trigger field notation section defines fixed position. |
| C-07 PM/Architect/Strategy evaluation shown | P | STEP 3 PM / STEP 4 Architect / STEP 5 Strategy with SQ sub-questions and verdict lines. All three roles present. |
| C-08 Tier flag respected | P | Tier extracted at STEP 1, written at output top, TIER-CRITICAL gates on `tier >= 2`. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 Coverage gap synthesis | P | Pre-printed cross-namespace risk statement with urgency levels BLOCKING/HIGH/MEDIUM in STEP 7. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | P | Rationale slot requires escape framing sentence; "a sentence that only confirms sufficiency...is a confirmatory echo and does not satisfy this slot." |
| C-11 Forbidden-output enumeration for auto-rules | P | All three rules carry "DO NOT mark...regardless of mock quality / mock content depth / evaluation outcome." |
| C-12 Zero-remaining confirmation gate | P | Canary confirmation block present with count = 0 requirement. |
| C-13 Verifiable role-step separation | P | Steps 3/4/5 separately completable, each with heading, sub-questions, verdict; STOP gate after each. |
| C-14 SQ answer citation in verdict traceability | P | "Sub-question answer that drove this verdict" field in eval-driven REAL-REQUIRED template. |
| C-15 Entity-naming sub-question grammar | P | All SQ forms use "Name the X" or "Name one X" grammar throughout all three roles. |
| C-16 Canary confirmation (prohibited under failure) | P | CANARY-FALSE-POSITIVE named as detectable protocol error; suppression protocol on failure. |
| C-17 Auto-flagged contamination guard | P | "auto-rule contamination" named as detectable error. |
| C-18 Inter-step gate with next-step reference | P | "DO NOT proceed to STEP N+1" throughout; forward-names blocked step. |
| C-19 Structured trigger notation | P | `trigger = {value}` canonical format; free-form mention outside field position named insufficient. |
| C-20 Contrastive MOCK-ACCEPTED rationale | Pt | Rationale slot asks to "name what this namespace has (or lacks) compared to a namespace that remains REAL-REQUIRED." Contrastive framing present, but single slot allows confirmatory escape — no Contrast sub-slot to guarantee structural contrast. Design hypothesis: C-20 PARTIAL. |
| C-21 SQ answer structural signal | F | Only "Sub-question answer" field with negative prohibition ("not a restatement of the verdict"). No "Artifact state" field, no present-tense grammar rule, no "verdict echo" named error. Positive structural signal absent. |
| C-22 Decision inversion framing | P | DEFAULT DECISION POSITION block present at skill level; "REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result." |
| C-23 Strategy SQ-1 anchor in structural position | F | MOCK-ACCEPTED template has only a single "Rationale:" slot. No `Structural position (Strategy SQ-1 tier decision):` labeled slot. SQ-1 referenced in instructional text only — advisory, not a named slot requirement. |
| C-24 Artifact state field propagation into next-steps | F | No Artifact state field in STEP 6 template. STEP 7 uses legacy conditional "if eval-driven" format. No explicit eval-driven sub-template. |

**Aspirational: 11.5/16 → 7.19 pts**

**V-01 Total: 60 + 30 + 7.19 = 97.19**

---

## V-02 — Strategy SQ-1 Labeled Slot Anchor

**Axis:** output-format | Labeled `Structural position (Strategy SQ-1 tier decision):` slot, PM-first, no inertia framing

### Essential

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Two-list output, all namespaces placed. |
| C-02 Automatic rule correctness | P | Three rules, forbidden-output, hard STOP. |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes, no paraphrase, NEVER invent. |
| C-04 Status write-back | P | STEP 8 mandatory, Edit tool, in-place. |
| C-05 Next-steps priority order | P | Ordering rule stated, four-section skeleton. |

**Essential: 5/5 → 60 pts**

### Recommended

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-06 Rule trigger named | P | Canonical trigger notation. |
| C-07 PM/Architect/Strategy evaluation shown | P | All three steps with SQ sub-questions. |
| C-08 Tier flag respected | P | Tier at top, TIER-CRITICAL gate correct. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 | P | Cross-namespace risk statement present. |
| C-10 | P | Two-slot template requires namespace-specific reasoning. |
| C-11 | P | Forbidden-output in all three auto-rules. |
| C-12 | P | Canary confirmation gate present. |
| C-13 | P | Three separate role steps with STOP gates. |
| C-14 | P | "Sub-question answer that drove this verdict" field present. |
| C-15 | P | "Name the X" sub-question grammar throughout. |
| C-16 | P | CANARY-FALSE-POSITIVE named; suppression protocol present. |
| C-17 | P | "auto-rule contamination" named. |
| C-18 | P | "DO NOT proceed to STEP N+1" all gates. |
| C-19 | P | Canonical trigger = notation with field-position rule. |
| C-20 Contrastive MOCK-ACCEPTED rationale | P | Two-slot template: `Structural position (Strategy SQ-1 tier decision)` forces specific decision + type classification; `Contrast` slot requires naming namespace type AND structural factor. SLOT-LABEL VIOLATION and CATEGORY ECHO named as detectable errors. |
| C-21 SQ answer structural signal | F | "Sub-question answer" field with negative prohibition only. No Artifact state field, no present-tense grammar rule, no verdict-echo named error. |
| C-22 Decision inversion framing | F | No DEFAULT DECISION POSITION block. MOCK-ACCEPTED and REAL-REQUIRED treated structurally symmetrically in framing. |
| C-23 Strategy SQ-1 anchor in structural position | P | `Structural position (Strategy SQ-1 tier decision):` labeled slot with SQ-1 as named input, type classification (STRUCTURAL-FORM vs TIER-GATING) as required output. SLOT-LABEL VIOLATION named as detectable error for generic fill. |
| C-24 Artifact state field propagation into next-steps | F | No Artifact state field in STEP 6. STEP 7 uses legacy conditional format "if eval-driven." No explicit eval-driven sub-template. |

**Aspirational: 13/16 → 8.13 pts**

**V-02 Total: 60 + 30 + 8.13 = 98.13**

---

## V-03 — Explicit Artifact State Propagation Sub-Templates

**Axis:** lifecycle-emphasis | Two explicit STEP 7 sub-templates (eval-driven + auto-flagged), Artifact state field with grammar spec, PM-first, no inertia framing

### Essential

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 | P | Two-list separation, STOP gate. |
| C-02 | P | Three rules, forbidden-output, hard STOP. |
| C-03 | P | Exact codes, no paraphrase. |
| C-04 | P | STEP 8 mandatory, Edit tool, in-place. |
| C-05 | P | Ordering rule stated, four-section skeleton. |

**Essential: 5/5 → 60 pts**

### Recommended

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-06 | P | Canonical trigger notation. |
| C-07 | P | All three roles present. |
| C-08 | P | Tier at top, TIER-CRITICAL gate. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 | P | Cross-namespace risk statement present. |
| C-10 | P | Rationale slot with namespace-specific reasoning. |
| C-11 | P | Forbidden-output in all three auto-rules. |
| C-12 | P | Canary confirmation gate present. |
| C-13 | P | Three separate role steps with STOP gates. |
| C-14 | P | "Sub-question answer" field present (pre-upgrade) — Artifact state slot satisfies citation traceability. |
| C-15 | P | "Name the X" grammar throughout. |
| C-16 | P | CANARY-FALSE-POSITIVE named; suppression protocol. |
| C-17 | P | "auto-rule contamination" named. |
| C-18 | P | "DO NOT proceed to STEP N+1" all gates. |
| C-19 | P | Canonical trigger = notation. |
| C-20 Contrastive MOCK-ACCEPTED rationale | Pt | Single "Rationale" slot with "name the tier decision it supports and explain why that decision type does not require real evidence." Explanatory but not structurally contrastive — no requirement to name a namespace that WOULD require real evidence. Partial credit: namespace-specific reasoning required, but contrast structure absent. |
| C-21 SQ answer structural signal | P | Artifact state field with full positive grammar spec: present-tense artifact-as-subject rule; three correct examples; verdict echo defined as named detectable error; grammatical subject detection rule stated. |
| C-22 Decision inversion framing | F | No DEFAULT DECISION POSITION block. No inertia framing at skill level. |
| C-23 Strategy SQ-1 anchor in structural position | F | MOCK-ACCEPTED has only "Rationale:" slot; no labeled SQ-1 structural position. |
| C-24 Artifact state field propagation into next-steps | P | Two explicit STEP 7 sub-templates: eval-driven entry requires `{Artifact state field from STEP 6}` unconditionally; auto-flagged entry requires `trigger: {trigger value}`. "Traceability break" named for misapplied format. Conditional removed entirely. |

**Aspirational: 13.5/16 → 8.44 pts**

**V-03 Total: 60 + 30 + 8.44 = 98.44**

---

## V-04 — SQ-1 Anchor Slot + Explicit Propagation Sub-Templates

**Axes:** output-format + lifecycle-emphasis | Labeled SQ-1 slot (C-23) + explicit sub-templates (C-24), Strategy-first ordering, Artifact state field, no inertia framing

### Essential

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 | P | Two-list separation, STOP gate. |
| C-02 | P | Three rules, forbidden-output, hard STOP. |
| C-03 | P | Exact codes, no paraphrase. |
| C-04 | P | STEP 8 mandatory, Edit tool, in-place. |
| C-05 | P | Ordering rule stated, four-section skeleton. |

**Essential: 5/5 → 60 pts**

### Recommended

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-06 | P | Canonical trigger notation. |
| C-07 | P | All three roles present (Strategy-first order). |
| C-08 | P | Tier at top, TIER-CRITICAL gate. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 | P | Cross-namespace risk statement present. |
| C-10 | P | Two-slot template with namespace-specific reasoning. |
| C-11 | P | Forbidden-output in all three auto-rules. |
| C-12 | P | Canary confirmation gate present. |
| C-13 | P | Three separate role steps with STOP gates. |
| C-14 | P | Artifact state field satisfies citation traceability. |
| C-15 | P | "Name the X" grammar throughout. |
| C-16 | P | CANARY-FALSE-POSITIVE named; suppression protocol. |
| C-17 | P | "auto-rule contamination" named. |
| C-18 | P | "DO NOT proceed to STEP N+1" all gates. |
| C-19 | P | Canonical trigger = notation. |
| C-20 Contrastive MOCK-ACCEPTED rationale | P | Two-slot template: labeled `Structural position (Strategy SQ-1 tier decision):` forces decision name + STRUCTURAL-FORM/TIER-GATING classification; `Contrast` slot requires naming namespace type AND structural factor. Both SLOT-LABEL VIOLATION and CATEGORY ECHO named. Strategy-first ordering means SQ-1 answer is available when MOCK-ACCEPTED template is filled. |
| C-21 SQ answer structural signal | P | Artifact state field with full positive grammar spec, verdict-echo named error, present-tense artifact-as-subject rule. |
| C-22 Decision inversion framing | F | No DEFAULT DECISION POSITION block. No inertia framing. REAL-REQUIRED is not structurally established as the default at skill level. |
| C-23 Strategy SQ-1 anchor in structural position | P | `Structural position (Strategy SQ-1 tier decision):` labeled slot with type classification requirement; SLOT-LABEL VIOLATION named. |
| C-24 Artifact state field propagation into next-steps | P | Two explicit STEP 7 sub-templates; eval-driven entry unconditionally requires Artifact state field; traceability break named for omission. |

**Aspirational: 15/16 → 9.38 pts**

**V-04 Total: 60 + 30 + 9.38 = 99.38**

---

## V-05 (Ceiling) — Inertia Framing + SQ-1 Anchor Slot + Explicit Propagation

**Axes:** inertia-framing + output-format + lifecycle-emphasis | All three R6 target criteria + all R5 V-05 ceiling criteria

### Essential

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Two-list output with "Remaining (awaiting evaluation — default: REAL-REQUIRED)" explicitly labeling the inertia position. STOP gate. |
| C-02 Automatic rule correctness | P | Three rules with forbidden-output language; auto-rule contamination named; "DO NOT apply Strategy, PM, or Architect evaluation to any auto-flagged namespace." |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes; "no paraphrase; NEVER invent codes." |
| C-04 Status write-back | P | STEP 8 mandatory, non-skippable; Edit tool; in-place; verification before confirming. |
| C-05 Next-steps priority order | P | "Critical first, evidence-heavy last" stated; four-section skeleton; ordering rule explicit. |

**Essential: 5/5 → 60 pts**

### Recommended

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-06 Rule trigger named | P | Canonical trigger = notation in all decision blocks; trigger field notation section at STEP 6. |
| C-07 PM/Architect/Strategy evaluation shown | P | STEP 3 Strategy / STEP 4 PM / STEP 5 Architect — all three roles with sub-questions and verdicts. |
| C-08 Tier flag respected | P | Tier extracted at STEP 1, written at top, TIER-CRITICAL gates on tier >= 2. |

**Recommended: 3/3 → 30 pts**

### Aspirational

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 Coverage gap synthesis | P | Pre-printed cross-namespace risk statement with BLOCKING/HIGH/MEDIUM urgency; "Required output" designation. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | P | `Structural position (Strategy SQ-1 tier decision):` slot requires specific decision name + type; Contrast slot requires namespace type + structural factor. SLOT-LABEL VIOLATION named as error for generic fill. |
| C-11 Forbidden-output enumeration for auto-rules | P | All three rules carry "DO NOT mark...regardless of...evaluation outcome" with specific enumerated contexts. |
| C-12 Zero-remaining confirmation gate | P | Canary confirmation block; "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." |
| C-13 Verifiable role-step separation | P | Strategy (STEP 3), PM (STEP 4), Architect (STEP 5) — each with own heading, evaluation question, sub-questions, verdict, and STOP gate. |
| C-14 Sub-question answer citation in verdict traceability | P | Artifact state field names specific section/element/gap; traces from observable artifact state to verdict. |
| C-15 Entity-naming sub-question grammar | P | All nine sub-questions use "Name the X" form; "not a yes/no" explicitly stated. |
| C-16 Canary confirmation (prohibited under failure) | P | CANARY-FALSE-POSITIVE named as detectable protocol error; suppression protocol with explicit output format when condition not met. |
| C-17 Auto-flagged contamination guard | P | "auto-rule contamination" named error; "any evaluation verdict applied to an auto-flagged namespace is void." |
| C-18 Inter-step gate with next-step reference | P | "DO NOT proceed to STEP N+1" throughout; forward-names blocked step. |
| C-19 Structured trigger notation | P | Canonical `trigger = {value}` in fixed position; trigger field notation section defines the rule; free-form mention outside field position named insufficient. |
| C-20 Contrastive MOCK-ACCEPTED rationale | P | Inertia framing + two-slot template: DEFAULT DECISION POSITION establishes escape context; `Structural position (Strategy SQ-1 tier decision):` slot forces classification; `Contrast` slot requires structural factor, not just category name. Both named errors enforce the template. |
| C-21 SQ answer structural signal | P | Artifact state field: present-tense artifact-as-subject rule with three correct examples and three verdict-echo anti-examples. Verdict echo defined as detectable by grammatical subject. The slot "exists to cite observable artifact state so the decision is traceable to the mock artifact independent of the role." |
| C-22 Decision inversion framing | P | DEFAULT DECISION POSITION block at skill level: "REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result." All three role SQ-3s framed as "gap that would KEEP THIS NAMESPACE IN ITS REAL-REQUIRED DEFAULT POSITION." |
| C-23 Strategy SQ-1 anchor in structural position | P | `Structural position (Strategy SQ-1 tier decision):` — slot label names Strategy SQ-1 as required input and type classification (STRUCTURAL-FORM vs TIER-GATING) as required output. "Do not write a general adequacy statement — that is a SLOT-LABEL VIOLATION." Anchor is a named slot requirement, not instructional text. |
| C-24 Artifact state field propagation into next-steps | P | STEP 7 provides two explicit format sub-templates: "Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}" and "Auto-flagged entry: /{skill-id} {topic} — trigger: {trigger value}". Traceability break named for omission; format error named for misapplication. |

**Aspirational: 16/16 → 10 pts**

**V-05 Total: 60 + 30 + 10.00 = 100.00**

---

## Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Total |
|------|-----------|-----------|-------------|--------------|-------|
| 1 | V-05 (Ceiling) | 60 | 30 | 10.00 | **100.00** |
| 2 | V-04 | 60 | 30 | 9.38 | **99.38** |
| 3 | V-03 | 60 | 30 | 8.44 | **98.44** |
| 4 | V-02 | 60 | 30 | 8.13 | **98.13** |
| 5 | V-01 | 60 | 30 | 7.19 | **97.19** |

**All 5 variations pass all essential criteria: yes**

---

## Excellence Signals from V-05

**What V-05 has that the single-axis variations lack:**

1. **Three-axis mutual reinforcement as a traceability chain.** The inertia block (C-22) establishes why escape is earned; the labeled SQ-1 slot (C-23) names the specific decision being escaped from; the explicit sub-templates (C-24) propagate the decision evidence unconditionally into next-steps. Each axis would be weaker alone — V-01 (inertia only) cannot close C-20 to PASS because the single Rationale slot has no Contrast enforcer; V-02 (labeled slot only) closes C-23 but the absence of inertia means the author can still write a confirmatory SQ-1 fill; V-03 (sub-templates only) propagates evidence but has nothing anchoring what gets propagated.

2. **Strategy-first ordering creates temporal alignment with the labeled SQ-1 slot.** The SQ-1 answer (the specific tier decision this namespace supports) is recorded at STEP 3 before the MOCK-ACCEPTED decision template is filled at STEP 6. This means when the author reaches `Structural position (Strategy SQ-1 tier decision):`, the answer already exists in the evaluation output. The slot label is pointing to a decision already named, not asking for new analysis. This is a structural guarantee that the labeled slot produces a decision citation rather than a generic adequacy statement.

3. **C-22 inertia framing propagates into SQ-3 grammar across all three roles.** Each role's SQ-3 is reframed from "Name one structural gap" to "Name the gap that would KEEP THIS NAMESPACE IN ITS REAL-REQUIRED DEFAULT POSITION." This means the evaluator is asking the escape-disqualification question, not the failure-detection question. The asymmetry is structural: the default is REAL-REQUIRED, so any gap disqualifies the escape rather than establishing a finding. This makes the MOCK-ACCEPTED decision a harder-to-reach conclusion — which is the design intent of C-22.

**R7 forward pointer from V-05 analysis:** The remaining gap is type-classification specificity in the Structural position slot. `STRUCTURAL-FORM vs TIER-GATING` as a type label does not yet require naming the architectural property that determines the type — a V-05 author can write "type: STRUCTURAL-FORM" without explaining *why* the namespace is structural-form (i.e., what architectural property puts it in that category). This would be the next C-25 target.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Strategy-first evaluation ordering creates temporal alignment with the labeled SQ-1 slot: the SQ-1 answer is recorded before the MOCK-ACCEPTED template is filled, making the labeled slot a citation of existing output rather than a request for new analysis — eliminating the risk of a generic fill", "Type-classification specificity in Structural position slot is not yet enforced: STRUCTURAL-FORM vs TIER-GATING as type labels do not require naming the architectural property that determines the classification (e.g., 'TIER-GATING because the decision requires observing live component state at tier boundaries') — a V-05 author can satisfy the slot with type label alone without the architectural property"]}
```
