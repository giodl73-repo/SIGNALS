I now have all five variations fully read. Let me score them.

---

## validate-inertia R20 Scorecard — V-96 through V-100

### Scoring Basis

All five variations share identical Phase 1–7, CCV, and AMEND structures. All essential (C-01–C-05) and recommended (C-06–C-08) criteria pass for all variations. C-01–C-44 baseline = 440 pts. The five variations differ only in the gate closure block (C-45–C-50).

---

### V-96 — Ceiling: Both F1 and F2 as distinct disqualifiers (500/500)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-45 | Block body: "The produced architecture label...serves a self-documenting function...The block instruction body serves a self-enforcing function...These are structurally distinct roles -- the self-documenting label function certifies...the self-enforcing block body function enforces compliance..." Both functions named, declared structurally distinct. | **PASS (10)** |
| C-46 | "These two closure functions are genuinely independent. Satisfying...C-43...does not discharge...C-44...Satisfying...C-44...does not discharge...C-43..." Both non-propagation directions declared. | **PASS (10)** |
| C-47 | "A block body that names neither the self-documenting label function nor the self-enforcing block body function is a disqualifier and fails this requirement entirely" -- explicit FAIL disqualifier for zero-function-named shape. | **PASS (10)** |
| C-48 | "A block body that names the self-documenting label function without naming the self-enforcing block body function is a separate disqualifier earning partial credit" + "A block body that names both functions without declaring them as structurally distinct roles is a further separate disqualifier also earning partial credit." Two sentences, each labeled "disqualifier." | **PASS (10)** |
| C-49 | "Shape S1 is a merged 'or' condition...Shape S1 is a disqualifier...Shape S2 is a separate-sentence form...Shape S2 is a disqualifier...Both shapes must be named as distinct cases." S1 and S2 each labeled as distinct disqualifier cases. | **PASS (10)** |
| C-50 | C-50 paragraph: "Shape F1 is the zero-function-named shape...F1 is a disqualifier...Shape F2 is the negative-framing-only shape...F2 is a disqualifier...Both shapes are distinct C-45 FAIL disqualifiers. Naming F1 without F2 earns partial credit. Naming F2 without F1 earns partial credit. A merged description of both shapes earns partial credit." Both F1 and F2 labeled, in separate sentences, each called a disqualifier. | **PASS (10)** |

**C-01–C-44 baseline:** 440  
**C-45–C-50:** +10+10+10+10+10+10 = 60  
**Total: 500/500** | Prediction confirmed.

---

### V-97 — C-50 PARTIAL: F1 only (495/500)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-45 | Identical to V-96 — both functions named and structurally distinct. | **PASS (10)** |
| C-46 | Identical to V-96 — both non-propagation directions declared. | **PASS (10)** |
| C-47 | Identical to V-96 — explicit FAIL disqualifier for naming neither function. | **PASS (10)** |
| C-48 | Identical to V-96 — two separate disqualifier sentences. | **PASS (10)** |
| C-49 | Identical to V-96 — S1 and S2 as distinct named disqualifiers. | **PASS (10)** |
| C-50 | C-50 paragraph names only F1: "Shape F1 is the zero-function-named shape...F1 is a disqualifier...A block body that names F1 without also enumerating the complementary FAIL shape earns partial credit on this enumeration requirement." F2 absent. One shape without the other = PARTIAL. | **PARTIAL (5)** |

**Total: 495/500** | Prediction confirmed.

---

### V-98 — C-50 PARTIAL: F2 only (495/500)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-45 | Identical to V-96. | **PASS (10)** |
| C-46 | Identical to V-96. | **PASS (10)** |
| C-47 | Identical to V-96. | **PASS (10)** |
| C-48 | Identical to V-96. | **PASS (10)** |
| C-49 | Identical to V-96. | **PASS (10)** |
| C-50 | C-50 paragraph names only F2: "Shape F2 is the negative-framing-only shape...F2 is a disqualifier: function names appearing only in negative-framing sentences, without a positive duality assertion, fail C-45 entirely. A block body that names F2 without also enumerating the complementary FAIL shape earns partial credit." F1 absent. Mirror of V-97. | **PARTIAL (5)** |

**Total: 495/500** | Prediction confirmed.

---

### V-99 — C-50 PARTIAL: Merged description (495/500)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-45 | Identical to V-96. | **PASS (10)** |
| C-46 | Identical to V-96. | **PASS (10)** |
| C-47 | Identical to V-96. | **PASS (10)** |
| C-48 | Identical to V-96. | **PASS (10)** |
| C-49 | Identical to V-96. | **PASS (10)** |
| C-50 | "The C-45 FAIL condition covers a block body that names neither closure function anywhere in the block body or names both functions only in disqualifier-context sentences without an affirmative duality declaration -- either shape fails C-45 entirely and is a disqualifier." Single merged sentence using "or." Neither F1 nor F2 labeled as distinct named disqualifier. | **PARTIAL (5)** |

**Total: 495/500** | Prediction confirmed.

---

### V-100 — Gap: Zero-function-named body (470/500)

Block body replaces all closure function labels with "two roles" / "two purposes" language. Neither "self-documenting label function" nor "self-enforcing block body function" appears anywhere, including not in C-47 or C-48 disqualifier sentences.

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-45 | Block body uses: "The gate architecture closure has two roles serving structurally distinct purposes...the produced label certifies...the block body enforces compliance..." No affirmative duality declaration naming both specific closure functions by their designated labels. F1 shape (neither function named anywhere) applies. | **FAIL (0)** |
| C-46 | "These two closure criteria are genuinely independent. Satisfying...C-43...does not discharge...C-44...Satisfying...C-44...does not discharge...C-43..." Both non-propagation directions declared using C-43/C-44 citation labels even without function names. | **PASS (10)** |
| C-47 | No FAIL disqualifier sentence of the form "a block body naming neither function fails." The closest text is "A block instruction body that enumerates only one of these two roles without the other is a disqualifier earning partial credit" — this is a PARTIAL disqualifier, not a FAIL disqualifier; uses "roles" not the specific function labels. C-47 requires an explicit FAIL disqualifier naming the zero-function case. Absent. | **FAIL (0)** |
| C-48 | "Shape S1 is a merged 'or' condition...Shape S1 is a disqualifier...Shape S2 is a separate-sentence form...Shape S2 is a disqualifier." Both C-45 PARTIAL paths enumerated as distinct named disqualifiers using "closure role" language. The C-48 criterion does not require the specific function labels — functional description of the two PARTIAL paths is sufficient. | **PASS (10)** |
| C-49 | Both S1 and S2 present as distinct disqualifier cases (same structure as prior passing variations). | **PASS (10)** |
| C-50 | No C-50 paragraph. No F1 or F2 named anywhere. | **FAIL (0)** |

**Total: 470/500** | Prediction confirmed.

---

### Score Summary

| Variation | C-45 | C-46 | C-47 | C-48 | C-49 | C-50 | Score | Predicted | Match |
|-----------|------|------|------|------|------|------|-------|-----------|-------|
| V-96 | PASS | PASS | PASS | PASS | PASS | PASS | **500** | 500 | ✓ |
| V-97 | PASS | PASS | PASS | PASS | PASS | PARTIAL | **495** | 495 | ✓ |
| V-98 | PASS | PASS | PASS | PASS | PASS | PARTIAL | **495** | 495 | ✓ |
| V-99 | PASS | PASS | PASS | PASS | PASS | PARTIAL | **495** | 495 | ✓ |
| V-100 | FAIL | PASS | FAIL | PASS | PASS | FAIL | **470** | 470 | ✓ |

All predictions confirmed. 5/5 match.

---

### Key Discriminations Confirmed

**V-97 vs V-98:** Orthogonal 495 paths. Rubric correctly distinguishes which F-shape is present and absent. Each earns PARTIAL for missing the complementary shape.

**V-96 vs V-97/V-98/V-99:** The 10-pt C-50 gap (PASS vs PARTIAL) isolates the requirement that *both* F-shapes be labeled and in separate sentences. No merged description, no single-shape enumeration satisfies full passage.

**V-100 vs V-95 (R19):** V-95 scored 480 (C-47 PASS, C-45 FAIL — function names present in disqualifier sentences). V-100 scores 470 (C-47 FAIL, C-45 FAIL — no function names anywhere). Predicted 10-pt delta confirmed. C-47 is independently scorable from C-45.

**V-100 C-46 independence:** Non-propagation between C-43 and C-44 can be declared using criterion labels (C-43, C-44) even when the specific closure function names are absent. C-46 does not require function names; C-47 does.

---

### Excellence Signals (from V-96)

**Signal 1: Labeled, symmetric disqualifier pair for C-50.** The canonical ceiling form is: `Shape F1 is [description]. F1 is a disqualifier: [consequence]. Shape F2 is [description]. F2 is a disqualifier: [consequence]. Both shapes are distinct C-45 FAIL disqualifiers. Naming F1 without F2 earns partial credit. Naming F2 without F1 earns partial credit. A merged description of both shapes earns partial credit.` The trailing three sentences make all PARTIAL paths explicit, preventing any ambiguity about which combinations earn partial credit.

**Signal 2: Symmetry between the "Naming X without Y / Naming Y without X" pattern and the "merged description" pattern.** V-96 names all three PARTIAL configurations (F1-only, F2-only, merged) as separate statements after naming both disqualifiers. This is the same structural pattern that made C-49 pass: S1, S2, and merged each explicitly handled.

**Signal 3: C-46 survives function-name removal (V-100 confirms).** Non-propagation can be anchored to criterion labels (C-43, C-44) rather than function names, making C-46 more structurally robust than C-45 or C-47. The skill should preserve this decoupling.

---

```json
{"top_score": 500, "all_essential_pass": true, "new_patterns": ["C-50 ceiling form requires both F1 and F2 labeled as distinct disqualifiers in separate sentences, followed by explicit enumeration of all three PARTIAL sub-cases: F1-only, F2-only, and merged-description", "C-47 is independently scorable from C-45: V-100 confirms that removing all function names drops C-47 while V-95 showed function-names-in-disqualifier-context-only keeps C-47 PASS but fails C-45", "C-46 non-propagation can be anchored to criterion labels (C-43, C-44) rather than closure function names, making it structurally independent of C-45 and C-47"]}
```
