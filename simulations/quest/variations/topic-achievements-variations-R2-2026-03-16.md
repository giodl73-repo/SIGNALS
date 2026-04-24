Written to `simulations/quest/golden/topic-achievements-variate-R2-2026-03-16.md`.

---

## Round 2 Summary

**Variation strategy**: 3 single-axis isolations of the R2 criteria, then 2 combinations.

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | C-11 only — synthesis-first gate | If a hard dependency ("do not proceed to Step 3 until this is written") is sufficient for C-11, the problem is sequencing, not quality |
| V-02 | C-12 only — consequence-backed rules | If enforcement clauses alone raise C-07/C-04 scores, they're doing double duty — one mechanism fixing two criteria |
| V-03 | C-13 only — Falsified structural isolation | If moving Falsified to its own step (with a placeholder in chain saying "see Step 4") guarantees full treatment, the skipping problem is attention/enumeration-mode, not framing |
| V-04 | C-11 + C-12 (no isolation) | Tests whether synthesis-first + enforcement clauses are synergistic before adding Falsified isolation; Falsified stays in chain with dedicated treatment |
| V-05 | C-11 + C-12 + C-13 (full stack) | All five aspirational criteria targeted simultaneously; risk is verbose prompt degrading essential compliance |

**Key design decisions:**

- V-03 uses a two-part technique: Step 3 says "classify chain except Falsified — leave placeholder `see Step 4`", and Step 4 is a dedicated Falsified-only step. This creates structural separation without requiring the model to remember an implicit rule.
- V-02's enforcement clauses are written as `*Enforcement: if X is absent — do Y*` italics blocks, visually distinct from the requirements they guard.
- V-05 includes a second enforcement clause in Step 4 that explicitly states "if Falsified appears only as a row within Step 3 chain — this step is not satisfied", closing the loophole where a model might try to satisfy both steps with one entry.
- All five variations preserve R1 V-04 baseline essentials: Glob pattern, 7-category coverage, EARNED/IN-PROGRESS/LOCKED schema, NEXT ACTION block.
