Written to `simulations/quest/golden/mock-ns-variate-R9-2026-03-15.md`.

---

## Round 9 summary

Since R8 achieved full convergence at 100 with both V-04 and V-05, R9 shifts from "which criteria to add" to "which structural form is most robust under execution pressure." All five variants target v8's 26 criteria; the discriminant is structural choice, not coverage.

| Variant | Axis | C-25 | C-26 | Predicted |
|---------|------|------|------|-----------|
| V-01 | Phrasing register ("you" address) | pass | pass | 100 |
| V-02 | Output format (tabular prohibition blocks) | pass | pass | 100 |
| V-03 | Inertia framing (consequence-first at S-3) | **FAIL** | pass | ~99.4 |
| V-04 | Role sequence + lifecycle (merged CLASSIFY-AND-FLAG + phase map) | pass | pass | 100 |
| V-05 | Full convergence + explicit 6-layer audit at S-3 close | pass | pass | 100 |

**V-03 is the load-bearing experiment.** Consequence-before-prohibition at S-3 is structurally incompatible with C-25 ("the guarantee stated above is broken" requires the C-21 affirmative closure to precede the consequence). V-03 deliberately omits C-25 to test whether the causal bridge it provides is independently necessary, or whether frontloading the failure cost achieves the same execution result. If V-03 performs equivalently to the full-convergence variants on real runs, C-25 is confirmed redundant when the consequence is front-loaded; if it underperforms, C-25's backward-reference framing is load-bearing.
