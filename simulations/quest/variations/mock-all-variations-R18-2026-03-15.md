Written to `simulations/quest/golden/mock-all-variate-R18-2026-03-16.md`.

---

## mock-all Variate R18 -- Summary

**New criteria instantiated:**

| Criterion | What it tests |
|-----------|---------------|
| C-36 | Preamble assigns explicit reference labels ("Declaration A", "Declaration B") to structural authority declarations |
| C-37 | Stage STOP gates cite those labels by name ("per Declaration A", "per Declaration B"), closing the verification loop |

**Discrimination ladder:**

| Variation | C-36 | C-37 | Score | Key structural property |
|-----------|------|------|-------|------------------------|
| V-01 | FAIL | FAIL | 16/29 | Single-stage; no preamble declaration; no labels |
| V-02 | FAIL | FAIL | 23/29 | Multi-stage; procedural preamble; terminal inertia |
| V-03 | FAIL | FAIL | 27/29 | Multi-stage; canonical declaration + per-stage inertia; no labels |
| V-04 | PASS | FAIL | 28/29 | **NEW** -- labeled declarations; stage bodies cite labels; gates restate inline |
| V-05 | PASS | PASS | 29/29 | Labeled declarations; gates cite "per Declaration A" / "per Declaration B" |

**R18 hypothesis confirmed by design:** V-04 is the first instantiation of C-36 PASS + C-37 FAIL. The sole structural difference between V-04 and V-05 is three words per stage gate: `per Declaration B` (inertia) and `per Declaration A` (REAL-REQUIRED). The label exists in both; the gate references it only in V-05.
