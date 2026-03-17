## quest-rubric Rubric v8

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/18 × 10)` — denominator /14 → /18

---

### Four new criteria from Round 7 excellence signals

All four target **partial-credit integrity** — the structural property C-10 tests at the formula level but not at the criterion level, the reproduction level, or the inter-boundary semantic level.

**C-23 — Per-criterion PARTIAL-CONDITION block**
V-03 and V-05 demonstrate this. C-10 tells you PARTIAL = 0.5 in the formula; C-23 tells you what evidence earns 0.5 for *this specific criterion*. Without it, evaluators interpret partial credit subjectively — violating C-02 at the partial-credit boundary. V-01 and V-04 fail: `verdict_weights` in SA-1 but no per-criterion condition.

**C-24 — Formula consistency across structural positions**
V-02 fails: SA-1 is `essential_pass / N * 60` (binary); FINAL RUBRIC is the weighted form. Two formula instances disagreeing on type leaves the governing formula ambiguous. V-03 gets PARTIAL: binary SA-1 formula + prose note + expanded FINAL RUBRIC — intent aligned, structure divergent.

**C-25 — FINAL RUBRIC anti-collapse formula guard**
V-04 introduces "Reproduce the weighted formula from SA-1 verbatim — do not collapse to binary counting." Same class as C-22 (reproduction fidelity) but guards formula structure rather than CM-NN identifiers. V-01 has `verdict_weights` in SA-1 but no guard — latent collapse risk.

**C-26 — VERDICT TIER DECLARATION inter-boundary block**
V-02, V-04, V-05 have a named block between `SPEC ANALYST: CLOSED` and `AUTHOR: OPEN` defining PASS/PARTIAL/FAIL semantics. Evaluator-facing grounding, findable by structure. V-01 and V-03 embed tier semantics only in SA-1 fields or formula comments.

---

### New failure modes

| FM | Name | Caught by |
|----|------|-----------|
| FM-09 | Conflicting formula type across structural positions | C-24 |
| FM-10 | Formula collapse at reproduction without guard | C-25 |
| FM-11 | Subjective partial-credit evaluation (no per-criterion condition) | C-23 |
| FM-12 | Floating tier semantics (no dedicated inter-boundary block) | C-26 |

---

### R7 Composite Scores under v8

| Variation | A/18 | Composite | Band |
|-----------|------|-----------|------|
| V-01 | 15/18 | 98.33 | Golden |
| V-02 | 15.5/18 | 98.61 | Golden |
| V-03 | 15.5/18 | 98.61 | Golden |
| V-04 | 17/18 | 99.44 | Golden |
| **V-05** | **18/18** | **100.00** | **Golden** |

**Baseline: R7 V-05 = 100.00 / Golden. No entering gap for Round 8.** All 18 aspirational criteria satisfied. Round 8 direction: identify unformalized structural properties, or test rubric generalization to non-quest-rubric skills.
