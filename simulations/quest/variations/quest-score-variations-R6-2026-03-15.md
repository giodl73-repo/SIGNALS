Written to `simulations/quest/golden/quest-score-variate-R6-2026-03-16.md`.

---

## Round 6 — 5 variations against v6 rubric

**New axes this round (targeting C-19, C-20, C-21):**

| Axis | Criterion | Injection point | Mechanism |
|------|-----------|-----------------|-----------|
| S | C-19 Priming-depth ceiling | JUDGE phase (before JUDGE STANDARD COMPLETE) | PRIMING CEILING NOTE: third-order entries are rubric-neutral; ceiling is at second-order self-reference; evaluator names it, not searches around it |
| T | C-20 Register-agnostic evaluation | ANALYST phase (before scoring table) | REGISTER NOTE: structural presence governs C-15–C-18 verdicts; imperative register ("CHECK:", "VERIFY:") satisfies on equal terms with declarative register |
| U | C-21 C-17/C-18 independence | ANALYST phase (after composite formula) | CRITERIA INDEPENDENCE NOTE: C-17 doesn't require C-15; C-18 requires C-15 even when C-17 PASS; explicit decoupling note mandated when they diverge |

**Variation structure:**

| Variation | Axes | Base | C-19 | C-20 | C-21 | Predicted score |
|-----------|------|------|------|------|------|-----------------|
| V-01 | S | R5 V-04 (P+Q+G+B+M) | PASS | FAIL | FAIL | 98.46 |
| V-02 | T | R5 V-04 | FAIL | PASS | FAIL | 98.46 |
| V-03 | U | R5 V-04 | FAIL | FAIL | PASS | 98.46 |
| V-04 | S+T+U+P+Q+G+B+M | R5 V-04 | PASS | PASS | PASS | 100 |
| V-05 | S+T+U+P+R+G+B+M+N | R5 V-05 | PASS | PASS | PASS | 100 |

**Key design decisions:**
- V-01–V-03 share the same base (R5 V-04) — the single-axis FAIL pattern confirms mutual independence; none of P+Q+G+B+M accidentally satisfies the new evaluator-behavior criteria
- V-04 vs V-05 architectural difference: V-05 fires the REGISTER NOTE *before* CHECK A/CHECK B (earlier injection than V-04) — if injection order affects C-20 compliance it will show as a spread
- V-05 adds Check D to the Verifier: enforces the C-17/C-18 independence note at the post-write audit stage, giving U two enforcement families (write-time ANALYST note + adversarial Verifier check)
- Formula updated throughout: `aspirational_pass / 13 * 10` (was `/10`)
