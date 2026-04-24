Written to `simulations/quest/golden/quest-score-variate-R5-2026-03-16.md`.

---

## Round 5 — v5 Rubric — Variations Summary

**Axis selection: 3 single-axis, 2 combos**

| # | Axes | Label | C-15 | C-16 | C-17 | C-18 | New relative to prior rounds |
|---|------|-------|------|------|------|------|------------------------------|
| V-01 | J | Lifecycle condensed (v5 baseline) | FAIL | FAIL | FAIL | FAIL | Clean v5 floor — all four new/carried criteria unmet |
| V-02 | K | Output format: per-output inline check + H-only | FAIL | PASS | PASS | FAIL | Tests synchronous vs asynchronous verification; isolates C-17 from C-18 |
| V-03 | L | Phrasing register: imperative + H + G | PASS | PASS | PASS | PASS | First register test; R4 V-05 structure in command voice |
| V-04 | H+G+S+T | Full envelope + *Why* field + synthesis gate | PASS | PASS | PASS | PASS | First to target C-10 and C-11 simultaneously alongside C-15..C-18 |
| V-05 | H+G+S+T+AF-8/9 | Third-order priming ceiling | PASS | PASS | PASS | PASS | AF-8 targets C-17's enforcement mechanism; AF-9 targets C-18's |

**Design rationale for each axis choice:**

- **V-01 (J — condensed)**: Needed because the v5 baseline has never been established. R4 V-01 established the v4 baseline; this does the same for v5. Without it, C-17/C-18 FAIL verdicts have no clean reference.

- **V-02 (K — inline check)**: Tests whether the *position* of verification (per-output, synchronous) matters for C-15. The v5 rubric's C-15 pass condition requires verification "after all output blocks" — this variation challenges that boundary directly. AF-6 in BEFORE YOU BEGIN still primes against C-15 misexecution, so C-17 should PASS even though C-15 FAILs.

- **V-03 (L — imperative register)**: The only axis not yet explored across all 4+ prior rounds. Carries R4 V-05's proven H+G structure verbatim but in imperative voice. If C-17/C-18 verdicts differ from V-04 (same mechanisms, specification voice), the difference is attributable purely to register.

- **V-04 (H+G+S+T)**: Integrates the two R5-v4 improvements (S-axis for C-11, T-axis for C-10) onto R4 V-05's H+G base. The first candidate for all-10-aspirational coverage in v5.

- **V-05 (+ AF-8/AF-9)**: Third-order priming. AF-8 says: "an AF entry targeting C-15/C-16 must itself be in BEFORE YOU BEGIN — misplacing it is C-17 FAIL, the same way AF-7 misplacement is C-16 FAIL." AF-9 says: "half-envelope is the C-18 failure mode — one end open." The ceiling test question: does naming the failure mode of the failure-mode enforcement mechanism (third order) produce any detectable compliance improvement, or does marginal AF-table length eliminate the benefit?
