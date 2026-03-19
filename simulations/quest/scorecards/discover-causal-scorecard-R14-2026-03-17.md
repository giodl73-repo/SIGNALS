## discover-causal Scorecard — Round 14

**Rubric:** v14 | **Max:** 230 pts | **Golden >= 225**

| Variation | Score | Tier |
|-----------|-------|------|
| V-01 (C-36 element-1 only) | **225** | Golden (floor) |
| V-02 (C-36 element-2 only) | **225** | Golden (floor) |
| V-03 (C-36 wrong location) | **225** | Golden (floor) |
| V-04 (C-36 paraphrase) | **225** | Golden (floor) |
| V-05 (Full C-36 ceiling) | **230** | Golden (ceiling) |

---

**C-36 fail analysis:**

- **V-01:** Element-1 present (field-absence-fails-C-33-separately), element-2 absent (`false`-vs-absent clause missing) → FAIL
- **V-02:** Element-2 present (`false`-vs-absent E-02 distinction), element-1 absent ("separately from C-31 fail" not named) → FAIL
- **V-03:** Both elements at Phase 3 ARTIFACT NOTE; Phase 6 silent → FAIL (wrong location)
- **V-04:** Both concepts paraphrased ("record `false` not absent"); no explicit "fails C-33 separately" or "E-02 gradeability distinction" naming → FAIL
- **V-05:** Both elements explicit in Phase 6 → PASS → 230/230

**V-01 vs V-02 symmetry confirmed:** Neither element alone satisfies C-36 — conjunctive requirement holds for C-36 exactly as it did for C-35 in R13.

**Closure:** The symmetric ARTIFACT audit chain is now fully closed. Every enforcement-chain ARTIFACT field (`preliminary_anchor_declared`, `anchor_updated_from_phase1`, `phase3_anchor_update_prohibited_form`, `phase1_anchor_prohibition_stated`) has a corresponding Phase 6 naming criterion with the same two-element structure.

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": []}
```
m R13 V-05)
- C-33 PASS -> C-36 gradeable in all variations

**C-36 result per variation: 0 pts (V-01 through V-04) | 5 pts (V-05)**

---

**C-36 fail analysis per variation:**

- **V-01:** Element-1 present -- Phase 6 names "absence of `phase3_anchor_update_prohibited_form` fails C-33 separately from the C-31 fail." Element-2 absent -- no `false`-vs-absent E-02 clause; rule does not name `false` as the correct value for the behavioral-fail case and does not contrast `false` with absent. Partial naming -> FAIL.

- **V-02:** Element-2 present -- Phase 6 states "the correct field value is `false` -- not absent; `false` vs absent is the E-02 gradeability distinction for `phase3_anchor_update_prohibited_form`." Element-1 absent -- rule does not state field absence fails C-33 *separately from the C-31 fail*; the independence of the two failure modes is not named. A model reading this prompt knows `false` is the right value but lacks the explicit rule that field absence constitutes a distinct, independent C-33 failure. Partial naming -> FAIL.

- **V-03:** Both elements placed as an ARTIFACT NOTE appended to the Phase 3 CONDITIONAL BRANCH after the ANCHOR-UPDATE PROHIBITED FORM. Phase 6 integration rules carry no corresponding C-36 rule. C-36 requires the synthesis point (Phase 6) specifically -- the same content at Phase 3 does not satisfy the fifth enforcement site. Wrong location -> FAIL.

- **V-04:** Phase 6 carries both C-36 concepts paraphrased: instructs to record the `phase3_anchor_update_prohibited_form` field whenever PATHWAY INCOMPLETE was declared, and to record `false` (not leave it absent) when Phase 3 carried no prohibited form. Does not use "fails C-33 separately from the C-31 fail" and does not name "E-02 gradeability distinction." Paraphrase without explicit structural naming -> FAIL. Parallel to how V-04 R13 failed C-35 for the same reason.

- **V-05:** Phase 6 integration rule carries both elements explicitly: (1) "absence of the field fails C-33 separately from the C-31 fail" and (2) "`false` vs absent is the E-02 gradeability distinction." Both elements present at synthesis point. PASS -> 5 pts -> 230/230.

---

**V-01 vs V-02 symmetry:** Both score 225. Confirms the conjunctive two-element requirement -- neither element alone satisfies C-36. Same structural confirmation as R13 V-01 vs V-02 for C-35.

**V-03 location specificity:** Both elements present in the prompt but at Phase 3, not Phase 6. Score 225, not 230. Confirms C-36 requires the synthesis phase specifically. The load-bearing function of Phase 6 naming -- detecting ARTIFACT failures at the synthesis point where all enforcement converges -- is not satisfied by upstream placement.

**V-04 paraphrase rejection:** Conceptual paraphrase ("record false not absent") carries the behavioral instruction without the structural naming C-36 requires ("fails C-33 separately from C-31 fail"; "E-02 gradeability distinction"). Scores 225. Confirms explicit structural naming is the pass condition.

---

**Cumulative enforcement chain state under v14:**

The symmetric ARTIFACT audit chain is now fully closed:

| ARTIFACT field | Behavioral criterion | Phase 6 naming criterion |
|----------------|----------------------|--------------------------|
| `preliminary_anchor_declared` | C-26 | C-29 |
| `anchor_updated_from_phase1` | C-30 | (self-named at Phase 6) |
| `phase3_anchor_update_prohibited_form` | C-31 | C-32 + **C-36** |
| `phase1_anchor_prohibition_stated` | C-27 | C-34 + **C-35** |

C-36 (targeting `phase3_anchor_update_prohibited_form`) and C-35 (targeting `phase1_anchor_prohibition_stated`) complete the synthesis-point naming chain. Every enforcement-chain ARTIFACT field now has a corresponding Phase 6 naming criterion with the same two-element structure: (1) field absence independently fails the criterion; (2) `false` vs absent is the E-02 gradeability distinction.

---

**EXCELLENCE SIGNALS from V-05:**

1. **Symmetric two-element rule structure:** Phase 6 carries the C-36 rule with both elements using the same structural form as the C-35 rule -- the pattern generalizes cleanly across both ARTIFACT field naming criteria.

2. **Explicit separation of failure modes:** "fails C-33 separately from the C-31 fail" distinguishes behavioral failure (C-31 -- no prohibited form at Phase 3) from audit failure (C-33 -- field absent), preventing a model from treating one as implying the other.

3. **E-02 gradeability distinction named at synthesis:** "`false` vs absent is the E-02 gradeability distinction" gives the scorer an unambiguous rule: `false` is correct audit for a behavioral fail; absent is a separate structural failure. This prevents the conflation error where a scorer marks C-33 FAIL based only on C-31 outcome.

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": []}
```
