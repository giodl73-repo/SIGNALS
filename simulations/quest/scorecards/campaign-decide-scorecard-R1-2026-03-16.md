## Scorecard — campaign-decide / Round 1

---

### Scoring Rubric Reference

| ID | Type | Weight |
|----|------|--------|
| C-01 | Essential | 12 pts |
| C-02 | Essential | 12 pts |
| C-03 | Essential | 12 pts |
| C-04 | Essential | 12 pts |
| C-05 | Essential | 12 pts |
| C-06 | Recommended | 10 pts |
| C-07 | Recommended | 10 pts |
| C-08 | Recommended | 10 pts |
| C-09 | Aspirational | 5 pts |
| C-10 | Aspirational | 5 pts |

Formula: `(E_pass/5 × 60) + (R_pass/3 × 30) + (A_pass/2 × 10)`

---

### V-01 — Inertia Framing

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | PASS | `prove-synthesize` block opens with `COMMIT / PAUSE / PIVOT / ABANDON` — explicit recommendation required |
| C-02 | PASS | `State confidence: High / Medium / Low` is a required output line |
| C-03 | PASS | Steps 1–6 map directly to the six sub-skills; each is a numbered section |
| C-04 | PASS | `COMPETITOR ZERO RULE` + Section 1 labelled "Inertia Analysis (required before named rivals)" — structurally enforced |
| C-05 | PASS | `Cite evidence from steps 1-5 by section reference` is an explicit instruction in step 6 |
| C-06 | PARTIAL | Numbered steps and section headers present, but no summary block or titled brief template. A model may produce prose rather than a document hierarchy. |
| C-07 | FAIL | No instruction to surface risks or counter-evidence anywhere in the prompt |
| C-08 | FAIL | `prove-hypothesis` is listed but hypothesis disposition (confirmed/refuted/inconclusive) is not required in step 6 |
| C-09 | FAIL | `High / Medium / Low` label required but no instruction to explain the rating |
| C-10 | FAIL | No conditioned next step instruction |

**Essential pass**: 5/5  
**Recommended pass**: 0/3 (C-06 partial, C-07 fail, C-08 fail)  
**Aspirational pass**: 0/2

**Composite**: (5/5 × 60) + (0/3 × 30) + (0/2 × 10) = **60**  
**Band**: Silver (all essential pass, score = 60 — borderline)

---

### V-02 — Output Format (Table-Driven Brief)

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | PASS | `Recommendation: [COMMIT / PAUSE / PIVOT / ABANDON]` is a required row in the Phase 6 schema |
| C-02 | PASS | `Confidence: [High / Medium / Low]` is an explicit schema row |
| C-03 | PASS | Six explicit phase headers with table schemas — coverage by construction |
| C-04 | PASS | Inertia rows appear first in Phase 1 table with `(Inertia rows must appear before any named rival rows.)` constraint |
| C-05 | PASS | `Because (cite by Phase): - [claim] because Phase [N], [section]` — two citation lines templated in Phase 6 |
| C-06 | PASS | Pre-defined table schema per phase, titled sections, summary recommendation block — structured format enforced |
| C-07 | PASS | `Counter-evidence: [one risk or caveat]` is a required row |
| C-08 | PASS | `Hypothesis outcome: [Confirmed / Refuted / Inconclusive]` is a required row in Phase 6 schema |
| C-09 | PASS | `Confidence rationale: [name the specific evidence gaps or strengths that drove this rating]` — explicit and descriptive |
| C-10 | PASS | `Next step: [if COMMIT: concrete action | if no-build: exit condition or revisit trigger]` — conditioned on recommendation |

**Essential pass**: 5/5  
**Recommended pass**: 3/3  
**Aspirational pass**: 2/2

**Composite**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**  
**Band**: Gold

---

### V-03 — Phrasing Register (Conversational)

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | PASS | Question 6 requires `COMMIT / PAUSE / PIVOT / ABANDON` as the first answer |
| C-02 | PASS | `State your confidence: High / Medium / Low` required in question 6 |
| C-03 | PARTIAL | Six questions map to six domains, but conversational framing offers no enforcement mechanism. A model may collapse domains or skip one without it being obvious. |
| C-04 | PASS | Question 1 explicitly opens with inertia before named alternatives — ordering constraint present |
| C-05 | PASS | `Show your work: link the recommendation explicitly to the evidence above` — explicit instruction |
| C-06 | FAIL | No section headers, no document structure template. Conversational framing actively discourages structured output unless the model adds it spontaneously. |
| C-07 | FAIL | No instruction to surface counter-evidence or risk |
| C-08 | FAIL | Hypothesis falsification defined in question 4 but no disposition (confirmed/refuted) required at verdict |
| C-09 | PASS | `Explain the rating — name what drove it, not just the label` — explicitly asks for calibration narrative |
| C-10 | PASS | `If committing: what is the next concrete step? / If not: what would need to change to revisit?` — conditioned on both paths |

**Essential pass**: 4/5 (C-03 partial → treat as FAIL for threshold)  
**Recommended pass**: 0/3  
**Aspirational pass**: 2/2

**Composite**: (4/5 × 60) + (0/3 × 30) + (2/2 × 10) = 48 + 0 + 10 = **58**  
**Band**: Bronze (essential fail on C-03)

---

### V-04 — Combined: Lifecycle + Inertia Framing

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | PASS | `Recommendation: [COMMIT / PAUSE / PIVOT / ABANDON]` required in Phase 6 |
| C-02 | PASS | `Confidence: [High / Medium / Low]` required in Phase 6 |
| C-03 | PASS | Six named phase gates — all domains must exist before Phase 6 gate fires |
| C-04 | PASS | `PHASE 1 — scout-competitors [INERTIA GATE]` with explicit "Complete the inertia analysis before listing any named competitor" |
| C-05 | PASS | `Evidence chain: [cite Phase 1-5 findings by section]` required in Phase 6 |
| C-06 | PASS | Named phase headers (`### PHASE N`), gate checks, structured Phase 6 block — document hierarchy enforced |
| C-07 | PASS | `Counter-evidence: [at least one risk or caveat]` required in Phase 6 |
| C-08 | PASS | `Hypothesis outcome: [Confirmed / Refuted / Inconclusive]` required in Phase 6 |
| C-09 | PASS | `Confidence rationale: [name the specific evidence gaps or strengths that drove the rating]` required |
| C-10 | PASS | `Next step if COMMIT: [concrete action, not "do more research"]` + `Next step if no-build: [exit condition or revisit trigger]` — conditioned and anti-vague |

**Essential pass**: 5/5  
**Recommended pass**: 3/3  
**Aspirational pass**: 2/2

**Composite**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**  
**Band**: Gold

---

### V-05 — Combined: Inertia + Evidence Traceability

| ID | Verdict | Evidence Note |
|----|---------|---------------|
| C-01 | PASS | `**Recommendation**: [COMMIT / PAUSE / PIVOT / ABANDON]` is a bolded required field in Phase 6 structure |
| C-02 | PASS | `**Confidence**: [High / Medium / Low]` required in Phase 6 structure |
| C-03 | PASS | Six numbered sub-skill steps each with required output specification |
| C-04 | PASS | `INERTIA-FIRST RULE` block at top — "before naming any product or company. This ordering is required, not optional." + type column (inertia/named) in competitor table |
| C-05 | PASS | `CITATION RULE` block — "at least three explicit 'because [Phase N, section]' citations" + minimum count enforced; `"If you cannot cite a claim, do not assert it"` |
| C-06 | PASS | Phase 6 uses bold Markdown headers for each required field; numbered steps with output specs provide document hierarchy |
| C-07 | PASS | `**Counter-evidence**: [one risk or caveat that could undermine the recommendation]` required |
| C-08 | PASS | `**Hypothesis Outcome**: [Confirmed / Refuted / Inconclusive]` required in Phase 6 |
| C-09 | PASS | `**Confidence rationale**: [explain what drove the rating — name specific evidence]` required |
| C-10 | PASS | `**Next step**: [COMMIT: concrete action | no-build: exit condition or revisit trigger]` — conditioned on both paths |

**Essential pass**: 5/5  
**Recommended pass**: 3/3  
**Aspirational pass**: 2/2

**Composite**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**  
**Band**: Gold

---

### Final Scorecard

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Band |
|------|-----------|-----------|-------------|--------------|-----------|------|
| 1 (tie) | **V-02** | 5/5 | 3/3 | 2/2 | **100** | Gold |
| 1 (tie) | **V-04** | 5/5 | 3/3 | 2/2 | **100** | Gold |
| 1 (tie) | **V-05** | 5/5 | 3/3 | 2/2 | **100** | Gold |
| 4 | V-01 | 5/5 | 0/3 | 0/2 | **60** | Silver |
| 5 | V-03 | 4/5 | 0/3 | 2/2 | **58** | Bronze |

**Predicted vs Actual**:  
Predicted: V-05 > V-04 > V-02 > V-01 > V-03  
Actual: Three-way tie at the top. V-02 outperformed prediction — table schemas are functionally as complete as named rules. V-03 correctly landed last.

---

### Excellence Signals (from Gold variations)

**Signal 1 — Schema-as-enforcement**: Pre-defining the exact rows/fields a model must fill (V-02, V-05) is more reliable than instructing behavior. A schema with `Hypothesis outcome: [Confirmed / Refuted / Inconclusive]` cannot be skipped the way a prose instruction can.

**Signal 2 — Named constraint blocks at the top**: Leading with `INERTIA-FIRST RULE` and `CITATION RULE` as labeled blocks (V-05) or `[INERTIA GATE]` labels (V-04) turns implicit expectations into named violations. A model that skips an unnamed convention may not skip a named rule.

**Signal 3 — Conditioned next steps with anti-vague guards**: V-04's `[concrete action, not "do more research"]` is the strongest C-10 formulation — it names the failure pattern to prevent it.

**Signal 4 — Citation minimum count**: V-05's `at least three explicit "because [Phase N, section]" citations` sets a quantified floor. Numeric minimums are harder to satisfy superficially than qualitative instructions.

**Signal 5 — C-09 phrasing that names the anti-pattern**: "name the specific evidence gaps or strengths that drove this rating" (V-02, V-04) outperforms "explain the rating" (V-03) because it names what specificity looks like.

---

**Separator between Gold variations**: V-02, V-04, and V-05 all score 100 because all ten criteria are structurally enforced. The tie-breaking dimension not captured in this rubric is *depth risk* — V-02's table-filling approach carries the highest risk of shallow cell content; V-05's named rules carry the lowest. For a rubric v2, a depth/substance criterion would differentiate them.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["schema-as-enforcement: pre-defined row schemas prevent omission more reliably than prose instructions", "named-constraint-blocks: RULE/GATE labels at top of prompt turn implicit expectations into named violations", "anti-vague guards: naming the failure pattern to prevent ('not do more research') is stronger than positive instruction alone", "citation minimum count: quantified floor ('at least three') harder to satisfy superficially than qualitative instruction"]}
```
