Now I have enough to score all five variations. Let me analyze each against the rubric.

---

## Scorecard — validate-inertia R19 (V-91 through V-95)

**Rubric version:** v19 | **Max points:** 490 | **Criteria in focus:** C-45 through C-49

---

### Scoring Basis

**Baseline assumption:** All variations share identical phase content (Phases 1–7), CCV, AMEND, and closure architecture through C-44. The single locus of variation is:
- V-91–V-94: the C-49 paragraph appended after the C-46 non-propagation block (identical C-45/C-46/C-47/C-48 text across all four)
- V-95: restructured closure that removes the positive duality declaration, leaving functions referenced only in disqualifier-context sentences

**Baseline score C-01–C-44:** 440 pts (5 essential × 10 + 3 recommended × 10 + 36 aspirational × 10)

---

### Criterion Analysis (C-45 through C-49)

#### C-45 — Gate architecture closure names both functions as structurally distinct roles

**Pass condition:** Block body makes a positive declaration naming the self-documenting label function and the self-enforcing block body function and declaring them structurally distinct.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-91 | "The gate architecture closure has two functions serving structurally distinct roles. The produced architecture label...serves a self-documenting function...The block instruction body serves a self-enforcing function...These are structurally distinct roles" — positive duality declaration present. | **PASS** |
| V-92 | Same closure text as V-91 for C-45 paragraph. | **PASS** |
| V-93 | Same closure text as V-91 for C-45 paragraph. | **PASS** |
| V-94 | Same closure text as V-91 for C-45 paragraph. | **PASS** |
| V-95 | Positive duality declaration removed. Both functions appear only in disqualifier-context sentences ("A block body that names neither...is a disqualifier"; "A block body that names the self-documenting label function without...is a separate disqualifier"). No affirmative "this closure has two functions serving structurally distinct roles" statement anywhere. | **FAIL** |

---

#### C-46 — Non-propagation between closure criteria declared in block body

**Pass condition:** Block body explicitly declares that satisfying C-43 does not discharge C-44 and vice versa.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-91–V-94 | "These two closure functions are genuinely independent. Satisfying the produced-label certification requirement (C-43:...) does not discharge the split-gate prohibition requirement (C-44:...). Satisfying the split-gate prohibition requirement (C-44:...) does not discharge the produced-label certification requirement (C-43:...). Both closure criteria must be independently satisfied." Full bidirectional non-propagation declared. | **PASS** |
| V-95 | "These two closure requirements (C-43 and C-44) are genuinely independent. Satisfying C-43 does not discharge C-44, and satisfying C-44 does not discharge C-43. Both must be independently satisfied." Non-propagation declared using criterion numbers (not function names) — still satisfies the declaration requirement. | **PASS** |

---

#### C-47 — C-45 FAIL condition declared as explicit disqualifier in block body

**Pass condition:** Block body names the case of naming neither closure function as an explicit disqualifier.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-91–V-94 | "A block body that names neither the self-documenting label function nor the self-enforcing block body function is a disqualifier and fails this requirement entirely — the absence of both functions means the closure architecture is undeclared." Explicit FAIL disqualifier present, names both functions. | **PASS** |
| V-95 | "A block body that names neither the self-documenting label function nor the self-enforcing block body function is a disqualifier and fails this requirement entirely — the absence of both functions means the closure architecture is undeclared." Same sentence present; functions named in negative framing satisfies C-47. | **PASS** |

---

#### C-48 — Both C-45 PARTIAL paths enumerated as distinct disqualifiers in block body

**Pass condition:** Two separate named disqualifier sentences, one per PARTIAL path (name-one-without-the-other; name-both-without-distinctness). Not merged into a single "or" sentence.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-91–V-94 | "A block body that names the self-documenting label function without naming the self-enforcing block body function is a **separate disqualifier** earning partial credit — naming one function omits one structural role and does not satisfy the duality requirement. A block body that names both functions without declaring them as structurally distinct roles is a **further separate disqualifier** also earning partial credit..." Two separate disqualifier sentences, each naming a distinct PARTIAL path. | **PASS** |
| V-95 | Same two sentences present in disqualifier-context structure. | **PASS** |

---

#### C-49 — Both C-48 PARTIAL shapes enumerated as distinct named cases in block body

**Pass condition:** Block body names both Shape S1 (merged "or" condition) and Shape S2 (separate sentences, outcome language, no "disqualifier" framing) as distinct named cases, each labeled a disqualifier. Either shape alone = PARTIAL. Merged description = PARTIAL.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-91 | "The C-48 PARTIAL taxonomy...has two structurally distinct shapes. Shape S1 is a merged 'or' condition...Shape S1 is a disqualifier...Shape S2 is a separate-sentence form using outcome language without explicit 'disqualifier' framing...Shape S2 is a disqualifier...Both shapes are distinct partial-credit disqualifiers. Both shapes must be named as distinct cases to satisfy this enumeration requirement." S1 and S2 each named, each labeled a disqualifier, in separate sentences. | **PASS (10)** |
| V-92 | C-49 paragraph names Shape S1 only ("Shape S1 is a merged 'or' condition...Shape S1 is a disqualifier: merging both PARTIAL paths into one sentence fails..."). S2 entirely absent. "A block body that enumerates only this shape without also naming the S2 shape satisfies one case but not both and earns partial credit." One shape named, one absent. | **PARTIAL (5)** |
| V-93 | C-49 paragraph names Shape S2 only ("Shape S2 is a separate-sentence form using outcome language...Shape S2 is a disqualifier..."). S1 entirely absent. "A block body that enumerates only this shape without also naming the S1 shape satisfies one case but not both and earns partial credit." Mirror of V-92. | **PARTIAL (5)** |
| V-94 | "The C-48 PARTIAL taxonomy...has partial-credit forms: a merged 'or' condition combining both PARTIAL paths into one sentence, or separate sentences using outcome language such as 'earns partial credit' without explicit 'disqualifier' framing, each earns partial credit and does not satisfy the full enumeration requirement." Both shapes described together in a single compound sentence — no "Shape S1" / "Shape S2" labels, no separate naming as distinct cases. | **PARTIAL (5)** |
| V-95 | Full S1/S2 taxonomy from V-91 present verbatim: both shapes named as distinct disqualifier cases in separate sentences. | **PASS (10)** |

---

### Composite Scores

| Variation | C-01–C-44 | C-45 | C-46 | C-47 | C-48 | C-49 | **Total** |
|-----------|-----------|------|------|------|------|------|-----------|
| V-91 | 440 | 10 | 10 | 10 | 10 | 10 | **490** |
| V-92 | 440 | 10 | 10 | 10 | 10 | 5 | **485** |
| V-93 | 440 | 10 | 10 | 10 | 10 | 5 | **485** |
| V-94 | 440 | 10 | 10 | 10 | 10 | 5 | **485** |
| V-95 | 440 | 0 | 10 | 10 | 10 | 10 | **480** |

All essential criteria (C-01–C-05): **PASS across all variations.**

---

### Ranking

| Rank | Variation | Score | Delta from ceiling |
|------|-----------|-------|--------------------|
| 1 | V-91 | 490/490 | — |
| 2 (tied) | V-92 | 485/490 | -5 |
| 2 (tied) | V-93 | 485/490 | -5 |
| 2 (tied) | V-94 | 485/490 | -5 |
| 5 | V-95 | 480/490 | -10 |

---

### Prediction Verification

| Variation | Predicted | Actual | Match? |
|-----------|-----------|--------|--------|
| V-91 | 490 | 490 | YES |
| V-92 | 485 | 485 | YES |
| V-93 | 485 | 485 | YES |
| V-94 | 485 | 485 | YES |
| V-95 | 480 | 480 | YES |

All predictions confirmed. Rubric discrimination is operating correctly.

---

### Excellence Signals from V-91 (490/490)

**Pattern 1 — Explicit shape labeling is the C-49 ceiling gate.**
V-91 uses named case labels ("Shape S1" and "Shape S2") and explicitly calls each one "a disqualifier" in a separate sentence. This is the structural difference between PASS and PARTIAL. V-92 names S1 but not S2; V-93 names S2 but not S1; V-94 describes both in a merged sentence without labels. All three land at 485. The ceiling requires both shapes named as distinct labeled disqualifier cases — labeling each one and separating them into distinct sentences is what makes the taxonomy complete.

**Pattern 2 — The 485-triple reveals orthogonal PARTIAL failure modes at identical point value.**
V-92, V-93, and V-94 represent three structurally distinct C-49 failures all scoring the same 5 pts. The rubric must distinguish them by structural shape (which shape is present or absent, vs. merged), not by score. This confirms that C-49 PARTIAL is a stable floor: no partial coverage of the taxonomy earns more than half credit, regardless of which coverage is provided.

**Pattern 3 — C-45 and C-49 are independently addable.**
V-95 confirms that C-49 PASS is achievable while C-45 FAIL — disqualifier-context function naming satisfies C-47, C-48, and C-49 without satisfying C-45's positive duality declaration requirement. The R19 gap (C-45 FAIL + full C-46/C-47/C-48/C-49) is closed at 480. This means the two layers of closure architecture (duality declaration vs. taxonomy enumeration) are genuinely orthogonal scoring axes.

---

```json
{"top_score": 490, "all_essential_pass": true, "new_patterns": ["C-49 PASS requires both shapes (S1 and S2) named as distinct labeled disqualifier cases in separate sentences — any partial coverage (one shape absent, or both merged without labels) caps at PARTIAL regardless of which shape is present", "The 485-triple (V-92/V-93/V-94) establishes three orthogonally distinct C-49 PARTIAL failure modes at identical point value, requiring rubric to discriminate by structural shape not score", "C-45 and C-49 are independently addable: V-95 confirms C-49 PASS is achievable with C-45 FAIL, closing the R19 gap at 480 and proving disqualifier-context function naming satisfies C-47/C-48/C-49 without satisfying C-45 positive duality declaration"]}
```
