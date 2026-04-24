## Round 7 Scoring — quest-rubric v7

**Rubric:** v7 (C-01–C-22) | **Formula:** `(E/5 × 60) + (R/3 × 30) + (A/14 × 10)`
**Entering gap:** C-10 only — universal fail through R6. All five variations target C-10 exclusively; all other R6 V-05 mechanics inherited.

---

### Criterion Evaluation Matrix

**Evaluation basis:** Prompt-design scoring — each variation evaluated on whether its protocol, if faithfully executed, produces output satisfying each criterion. Trace artifact = placeholder; no execution output.

#### Essential (C-01–C-05) — all variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Skill identity declared | PASS | PASS | PASS | PASS | PASS |
| C-02 | Criteria are testable | PASS | PASS | PASS | PASS | PASS |
| C-03 | Pass condition enforced | PASS | PASS | PASS | PASS | PASS |
| C-04 | Scoring formula explicit | PASS | PASS | PASS | PASS | PASS |
| C-05 | Tier structure present | PASS | PASS | PASS | PASS | PASS |

Evidence (all): SA-1 SCHEMA BLOCK fills `skill:` field (C-01); INERTIA-RECORD Status-Quo test is binary evaluable (C-02); CRITERION GATE = OPEN/BLOCKED enforces mandatory language (C-03); FINAL RUBRIC scoring section in all five has an explicit weighted formula with denominators (C-04 — note V-02's SA-1 is binary but FINAL RUBRIC overrides); Essential/Recommended/Aspirational tiers declared in SA-1 `weight_values` (C-05).

C-04 note on V-02: SA-1 `scoring_formula` is `essential_pass / N_essential * 60` (binary). However, the FINAL RUBRIC scoring section explicitly restates the weighted form. Since C-04 evaluates whether the definitive formula is explicit and includes denominators — and the FINAL RUBRIC formula does — PASS stands. The SA-1/FINAL RUBRIC tension is a C-10 question, not C-04.

---

#### Recommended (C-06–C-08) — all variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Failure modes cataloged | PASS | PASS | PASS | PASS | PASS |
| C-07 | Specificity test included | PASS | PASS | PASS | PASS | PASS |
| C-08 | Version and date stamped | PASS | PASS | PASS | PASS | PASS |

Evidence: A-1 requires minimum 3 blocking + 2 degrading failure modes (C-06); Status-Quo Rubric framing + SA-2 CONVERSION-MAP produce at least one specificity criterion with Boolean test (C-07); SA-1 SCHEMA BLOCK has `version: 1` and `date:` fields (C-08).

---

#### Aspirational (C-09–C-22)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Coverage of all output sections | PASS | PASS | PASS | PASS | PASS |
| **C-10** | **Partial credit in formula** | **PASS** | **PARTIAL** | **PASS** | **PASS** | **PASS** |
| C-11 | External enforcement gate | PASS | PASS | PASS | PASS | PASS |
| C-12 | Failure modes before criteria | PASS | PASS | PASS | PASS | PASS |
| C-13 | Foil pair present | PASS | PASS | PASS | PASS | PASS |
| C-14 | Closed category enumeration | PASS | PASS | PASS | PASS | PASS |
| C-15 | Specificity prohibitions converted | PASS | PASS | PASS | PASS | PASS |
| C-16 | Fields have structural home | PASS | PASS | PASS | PASS | PASS |
| C-17 | SCHEMA BLOCK positionally first | PASS | PASS | PASS | PASS | PASS |
| C-18 | CONVERSION-MAP boolean gate | PASS | PASS | PASS | PASS | PASS |
| C-19 | Identifier citation in canonical row | PASS | PASS | PASS | PASS | PASS |
| C-20 | Author Entry Gate structural block | PASS | PASS | PASS | PASS | PASS |
| C-21 | Phase-completion status token at every boundary | PASS | PASS | PASS | PASS | PASS |
| C-22 | FINAL RUBRIC citation-retention guard | PASS | PASS | PASS | PASS | PASS |

---

**C-10 evidence by variation:**

**V-01 — PASS.** SA-1 declares `verdict_weights: PASS: 1.0 / PARTIAL: 0.5 / FAIL: 0.0` and `scoring_formula: sum(essential_verdict_weights) / N_essential`. FINAL RUBRIC formula: `where: PASS → weight 1.0 | PARTIAL → weight 0.5 | FAIL → weight 0.0`. Both the schema template and the scoring section are weighted. Formula distinguishes PARTIAL from PASS at two structural points.

**V-02 — PARTIAL.** SA-1 `scoring_formula` is `essential_pass / N_essential * 60` — a binary count with no `verdict_weights` field. The VERDICT TIER DECLARATION defines PARTIAL semantically between SA close and Author open. FINAL RUBRIC says "Apply the verdict weights from VERDICT TIER DECLARATION (PASS=1.0, PARTIAL=0.5, FAIL=0.0)" and restates the weighted formula. Result: FINAL RUBRIC is weighted; SA-1 is binary. Structural inconsistency — a binary formula exists in the document even though the definitive scoring section is weighted. The pass condition "no binary collapse" is partially violated by the SA-1 template. PARTIAL awarded: FINAL RUBRIC weighted formula is present (0.5 pass value), but the binary SA-1 formula constitutes unresolved collapse in schema context.

**V-03 — PASS.** SA-1 `scoring_formula` is binary with a note: `note: PARTIAL verdicts count as 0.5 in the numerator for recommended and aspirational tiers`. Per-criterion PARTIAL-CONDITION blocks (sub-step A2d) give the 0.5 weight observable content per criterion. FINAL RUBRIC has the explicit expanded form: `((E_pass + 0.5 * E_partial) / N_essential * 60) + ...`. The expanded formula is unambiguous; C-10 PASS.

**V-04 — PASS.** SA-1 has `verdict_weights` field AND weighted formula template (from V-01). VERDICT TIER DECLARATION defines PARTIAL semantically before Author opens (from V-02). FINAL RUBRIC says "Reproduce the weighted formula from SA-1 verbatim — do not collapse to binary counting" — explicit anti-stripping guard. Three-layer enforcement. C-10 PASS.

**V-05 — PASS.** Inherits all V-04 mechanisms plus V-03's per-criterion PARTIAL-CONDITION. SA-1 has `verdict_weights` + `partial_condition` in `criteria_fields`. FINAL RUBRIC has both compact and expanded forms. The expanded form `((E_pass + 0.5 * E_partial) / N_essential * 60)` makes the 0.5 coefficient explicit in variable form. Strongest C-10 implementation. PASS.

---

**Other aspirational criteria — selected evidence:**

- **C-11:** AUTHOR: BLOCKED with specific artifact identifiers + STRUCTURAL VERIFICATION + AUDITOR: CLOSED preconditions = named rejection steps. PASS all.
- **C-12:** A-1 (failure modes) precedes A-2 (criteria) in all output templates. PASS all.
- **C-13:** CALIBRATION-PAIR block required after every INERTIA-RECORD. Concrete STATUS-QUO RUBRIC vs. GROUNDED pair. PASS all.
- **C-14:** `category_values: [correctness, depth, format, coverage, behavior]` — closed five-value enumeration in SA-1. PASS all.
- **C-17:** SA-1 SCHEMA BLOCK is the first element inside SPEC ANALYST: OPEN, before failure modes, criteria, and Auditor. PASS all.
- **C-21:** All four boundaries in every template: `SPEC ANALYST: CLOSED` (SA close), `AUTHOR: [BLOCKED / OPEN]` (Author open), `AUTHOR: CLOSED` (Author close), `AUDITOR: OPEN` (Auditor open). String-scannable tokens, not checklists. PASS all.
- **C-22:** V-01 through V-04: "Retain CM-NN citations in Pass Condition for specificity criteria — do not simplify during reproduction." V-05 adds "or omit." All PASS. V-05 marginally stronger guard.

---

### Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| E (C-01–C-05) | /5 × 60 | 5 | 5 | 5 | 5 | 5 |
| R (C-06–C-08) | /3 × 30 | 3 | 3 | 3 | 3 | 3 |
| A (C-09–C-22) | /14 × 10 | 14 | 13.5 | 14 | 14 | 14 |
| **E score** | | **60.00** | **60.00** | **60.00** | **60.00** | **60.00** |
| **R score** | | **30.00** | **30.00** | **30.00** | **30.00** | **30.00** |
| **A score** | | **10.00** | **9.643** | **10.00** | **10.00** | **10.00** |
| **Composite** | | **100.00** | **99.64** | **100.00** | **100.00** | **100.00** |
| **Band** | | Golden | Golden | Golden | Golden | Golden |
| **All essential PASS?** | | Yes | Yes | Yes | Yes | Yes |

---

### Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tied) | V-04 | 100.00 | Dual-mechanism: SA-1 weighted template + VERDICT TIER DECLARATION + anti-collapse guard |
| 1 (tied) | V-05 | 100.00 | Triple-mechanism: all V-04 mechanics + per-criterion PARTIAL-CONDITION |
| 1 (tied) | V-01 | 100.00 | Template-only: SA-1 verdict_weights + weighted FINAL RUBRIC formula; simplest path |
| 1 (tied) | V-03 | 100.00 | Lifecycle-only: per-criterion PARTIAL grounding + explicit expanded formula |
| 5 | V-02 | 99.64 | SA-1 binary template creates structural inconsistency despite VERDICT TIER DECLARATION |

**Preliminary anchor confirmed: V-04.** V-04 and V-05 both achieve 100.00. The per-criterion PARTIAL-CONDITION step in V-05 is not load-bearing for C-10 (V-04 cracks it without it). V-05's A2d overhead is redundant for this criterion target. V-04 is the minimal combination that cracks C-10 reliably. V-05 should be evaluated for secondary benefits (foil pair quality, specificity conversion depth) as a separate question.

**V-02 degradation explained:** Isolating the phrasing-register axis while leaving SA-1 binary creates a binary formula in the schema block. Even with the VERDICT TIER DECLARATION bridging semantics and the FINAL RUBRIC carrying the weighted formula, the structural inconsistency in SA-1 constitutes a residual binary collapse. V-02 confirms that semantic grounding alone (without template change) does not fully resolve C-10 at the structural level. C-10 requires the template to be weighted from the start.

---

### Excellence Signals from Top-Scoring Variations

The four mechanisms that separately and jointly crack C-10:

**Signal 1 — Template-commit in SA-1 (V-01, V-04, V-05):** Placing `verdict_weights: PASS: 1.0 / PARTIAL: 0.5 / FAIL: 0.0` in the SA-1 YAML schema makes the model commit to weighted scoring before writing any criterion. The model fills what the template shows; if the template is weighted, the output is weighted. This is the same principle as the PHASE STATUS token — put the protocol in the structure, not in advisory text.

**Signal 2 — Anti-collapse reproduction guard in FINAL RUBRIC (V-04, V-05):** The "do not collapse to binary counting — reproduce the weighted formula from SA-1 verbatim" instruction in the FINAL RUBRIC section is structurally equivalent to the C-22 CM-NN citation-retention guard. Both address the reproduction stripping problem: the model may correctly produce a structure early in the lifecycle but simplify it at reproduction. The explicit "do not collapse" guard prevents regression at the final step. Pattern: every structural commitment needs a corresponding anti-stripping guard at reproduction.

**Signal 3 — Operational per-criterion grounding (V-03, V-05):** The PARTIAL-CONDITION sub-step forces the model to name a specific observable partial state per criterion before writing the CRITERION row. This gives the `0.5` weight concrete content — not just a variable in a formula, but a defined state the evaluator can detect. This makes the formula meaningful rather than formally present. Secondary benefit: improves PASS/PARTIAL/FAIL boundary precision for the evaluator using the rubric.

**Signal 4 — V-02 negative signal:** Semantic grounding without template change is insufficient. The VERDICT TIER DECLARATION correctly defines PARTIAL but leaves the SA-1 formula binary. The formula template governs the output more strongly than a declaration that precedes it. Template change (V-01) beats semantic declaration (V-02) as a single-axis mechanism. Implications for design: when the model produces from a template, change the template first; don't expect a preceding declaration to override template inertia.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Template-commit in SA-1: placing verdict_weights field in YAML schema makes model commit to weighted scoring before any criterion is written — template inertia enforces the output shape", "Anti-collapse reproduction guard in FINAL RUBRIC: explicit do-not-collapse instruction mirrors C-22 citation-retention guard and prevents binary stripping at the reproduction step", "Operational per-criterion grounding: PARTIAL-CONDITION sub-step forces observable partial state per criterion, giving the 0.5 coefficient concrete content rather than a named variable"]}
```
