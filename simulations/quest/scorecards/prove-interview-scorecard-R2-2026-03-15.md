# prove-interview — Round 2 Scoring

**Rubric:** v2 | **Formula:** `(E/5 × 60) + (R/3 × 30) + (A/4 × 10)` | PARTIAL = 0.5

---

## Scoring Notes

V-01 and V-02 have partial or full prompt bodies visible. V-03, V-04, V-05 are scored from axis descriptions — scores carry uncertainty; marked with ⚠.

---

## Criterion-Level Scorecard

| Criterion | Weight | V-01 | V-02 | V-03 ⚠ | V-04 ⚠ | V-05 ⚠ |
|-----------|--------|------|------|---------|---------|---------|
| **C-01** Persona identity declared | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** Prior knowledge scoped | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Answers in persona voice | essential | PASS | PARTIAL | PASS | PASS | PASS |
| **C-04** Evidence explicitly extracted | essential | PASS | PARTIAL | PASS | PASS | PARTIAL |
| **C-05** SURPRISING/CONFIRMING labeled | essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** Questions probe concerns | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Multiple distinct personas | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Evidence signal-typed | recommended | PASS | FAIL | PARTIAL | PARTIAL | FAIL |
| **C-09** Cross-interview synthesis | aspirational | PASS | FAIL | PARTIAL | PARTIAL | FAIL |
| **C-10** Simulation fidelity annotated | aspirational | PASS | FAIL | PARTIAL | PARTIAL | FAIL |
| **C-11** Voice divergence acknowledged | aspirational | PASS | FAIL | FAIL | FAIL | PASS |
| **C-12** Follow-up origin visible | aspirational | PASS | PASS | FAIL | PARTIAL | PASS |

### Evidence Notes

**V-01:**
- C-05: Expectation Register in Step 1 makes the format structurally mandatory — every label must cite a register row. INCONCLUSIVE option prevents forced labeling.
- C-08: Step 3 lists signal type options explicitly (`adoption-risk`, `feasibility-concern`, etc.)
- C-11: Step 6 "Voice Observation" is a dedicated deliverable with example form.
- C-12: Follow-up marked `triggered by: "[exact phrase]"` — quoting is required, not optional.

**V-02:**
- C-03: "Listen" framing implies persona voice but no explicit requirement that answers sound like the persona specifically. PARTIAL.
- C-04: Conversational/discovery register — no dedicated extraction phase in visible text. PARTIAL (implicit expectation that the interviewer would summarize what they learned, but no structural enforcement).
- C-08: Signal typing not present in visible text; not aligned with V-02's axis focus.
- C-09/C-10/C-11: Not addressed. V-02 is a single-axis variation targeting C-05 + C-12 only.
- C-12: PASS — the inline example "because you just said X, I want to ask..." directly models the required behavior. The prompt's own phrasing becomes the template.

**V-03 ⚠:**
- C-05: PASS — Phase 0 expectation declaration is the axis; creates traceable priors structurally.
- C-11/C-12: Not in V-03's axis. FAIL/FAIL. This variation solves one of the three R2 gaps, not all three.
- C-08/C-09/C-10: Assumed present from base skill structure but not verified. PARTIAL.

**V-04 ⚠:**
- C-05: PASS — Q1 current-practice answer becomes the prior the label must reference. Structural, not authorial.
- C-11: Not addressed. FAIL.
- C-12: PARTIAL — the Q1→Q3 prior reference implies answer-anchoring but doesn't explicitly require quoting the trigger phrase.
- C-06: PASS — current-practice questions naturally probe role-specific concerns; skeptic-first ordering ensures adversarial probing.

**V-05 ⚠:**
- C-04: PARTIAL — combines V-02's conversational register (which had no dedicated extraction phase) with voice divergence layer. Extraction still not structurally enforced.
- C-08: Not aligned with V-05's axis. FAIL.
- C-09/C-10: Not addressed. FAIL.
- C-11: PASS — the entire axis; voice management framed as craft problem makes the meta-observation a natural deliverable.
- C-12: PASS — inherits V-02's follow-up attribution phrasing.

---

## Composite Scores

| Variation | E (×60) | R (×30) | A (×10) | **Composite** | All Essentials Pass? | Threshold |
|-----------|---------|---------|---------|---------------|---------------------|-----------|
| V-01 | 5/5 → 60 | 3/3 → 30 | 4/4 → 10 | **100** | YES | Golden |
| V-04 ⚠ | 5/5 → 60 | 2.5/3 → 25 | 1.5/4 → 3.75 | **88.75** | YES | Passing |
| V-03 ⚠ | 5/5 → 60 | 2.5/3 → 25 | 1/4 → 2.5 | **87.5** | YES | Passing |
| V-05 ⚠ | 4.5/5 → 54 | 2/3 → 20 | 2/4 → 5 | **79** | C-04 partial | Below Golden |
| V-02 | 4/5 → 48 | 2/3 → 20 | 1/4 → 2.5 | **70.5** | C-03/C-04 partial | Below threshold |

*C-09 applies to all variations (all have ≥ 2 subjects); denominator stays 4.*

---

## Ranking

1. **V-01 — 100** All 12 criteria explicitly and structurally enforced.
2. **V-04 ⚠ — 88.75** All essentials pass; C-11 gap; C-12 partial; strong recommended layer.
3. **V-03 ⚠ — 87.5** All essentials pass; C-11 and C-12 both fail; focused lifecycle fix only.
4. **V-05 ⚠ — 79** C-04 partial; solves C-11 and C-12 but leaves extraction unstructured.
5. **V-02 — 70.5** C-03 and C-04 both partial; C-08/C-09/C-10/C-11 absent; single-axis scope.

---

## Excellence Signals — from V-01

**1. Structural inevitability over instruction**
The Expectation Register is filled *before* any transcript begins. This makes C-05 compliance automatic: the SURPRISING/CONFIRMING label must cite a register cell, not an authorial judgment call about what felt surprising. The prior expectation exists on paper before the interview starts.

**2. INCONCLUSIVE as a third label**
R1's gap was forced labeling — moments that didn't clearly confirm or surprise got mislabeled. V-01 provides an INCONCLUSIVE option with its own format, allowing honest resolution. This makes the SURPRISING/CONFIRMING labels more trustworthy when they appear.

**3. Named phases with single-criterion ownership**
Each step (1–6) covers exactly one rubric concern. Step 1 → C-01/C-02/C-05 setup. Step 2 → C-03/C-06/C-12. Step 3 → C-04/C-08. Step 4 → C-09. Step 5 → C-10. Step 6 → C-11. No criterion is left to the author to remember — the structure demands it.

**4. Inline examples as inherited templates**
Step 6 doesn't describe C-11 — it provides an example form: `"[Subject A] used the phrase '...' where [Subject B] would have said '...' — the difference reflects [contrast]."` The simulation can inherit the form directly without interpretation.

**5. Register cross-reference across phases**
The register created in Step 1 is explicitly consumed in Step 2 (header includes register cell verbatim) and Step 4 (register audit: SURPRISING/CONFIRMING/INCONCLUSIVE by subject name). The document cites itself, creating an internal consistency check.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["expectation-register-as-structural-prior-makes-C05-format-inevitable", "INCONCLUSIVE-third-label-prevents-forced-SURPRISING-CONFIRMING-compliance", "voice-observation-as-named-deliverable-step-not-instruction"]}
```
