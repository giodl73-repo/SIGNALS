Written to `simulations/quest/golden/quest-score-variate-R12-variations-2026-03-15.md`.

---

**R12 summary:**

| Variation | Axis | C-09 | C-28 | C-29 | C-32 | Composite |
|-----------|------|------|------|------|------|-----------|
| V-01 | APA on role-sequence | PASS | PARTIAL | FAIL | PASS | ~288 |
| V-02 | PRR on role-sequence | FAIL | PASS | FAIL | PASS | ~292 |
| V-03 | IRQ on table-format | FAIL | PARTIAL | PASS | PASS | ~288 |
| V-04 | APA + PRR on V-04 R11 | PASS | PASS | PASS | PASS | 310 |
| V-05 | APR fix on V-05 R11 | PASS | PASS | PASS | PASS | 310 |

**Three open gaps closed:**
- **C-09**: 5-mode anti-pattern anchor added in V-01 and V-04 (Failure Modes A–E with typical outputs and closing mechanisms)
- **C-28**: Per-entry routing annotations in PROHIBITED CONTENT CATEGORIES in V-02 and V-04 (each category names its ANALYST destination)
- **C-29**: Dual-scope VERIFIER in V-03 with Question 1 (type-level) + Question 2 (intra-run) explicit in V-03; inherited in V-04

**C-32 gap closed in V-05**: `"do not describe the evidence"` → `"do not paraphrase the evidence"` — one phrase, one PARTIAL→PASS.

**Formula updated** from `/23 * 220` to `/25 * 220` across all five variations.

**Two paths to 310:** V-04 (combination on dual-scope base) and V-05 (minimal fix on full-stack base).
