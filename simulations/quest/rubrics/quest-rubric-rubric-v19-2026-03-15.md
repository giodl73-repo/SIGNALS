v19 rubric written to `simulations/quest/golden/quest-rubric-variate-v19-R18-2026-03-16.md`.

**What changed:**

**C-49 — Failure-mode clause format-templated with mandatory criterion-ID slot**
Extends C-47. The criterion-ID inclusion in Phase 8.5 failure-mode clauses is enforced by a FORMAT TEMPLATE with a mandatory `[C-NN]` slot — e.g., `"Absent this path, [C-NN] is unenforced at Phase 8.5 entry"` — rather than by prose instruction. A builder following the template cannot omit the criterion ID without leaving a visible unfilled placeholder. V-01 of R18 demonstrates PASS C-47 / FAIL C-49 (criterion ID present, no template slot enforcing it), establishing independence.

**C-50 — Full criterion-span claim in STATUS QUO COMPETITOR foil items**
Extends C-48. Each foil item enumerates every passing criterion between span-start and the failing criterion — e.g., `"passes C-41, C-42, C-43, C-44, and C-45 while failing C-46"` — rather than a subset. Converts the foil item from a partial bidirectional discrimination statement to a precision criterion-lattice locator with no gaps on the pass side. V-02 of R18 demonstrates PASS C-48 / FAIL C-50 (some passing criteria named, not full span), establishing independence.

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/42 × 10)` — denominator /40 → /42 (C-09 through C-50)

**Baseline for R19:** Variations satisfying C-47 + C-48 but lacking template enforcement (C-49 FAIL) or partial pass-span (C-50 FAIL) score 40/42 × 10 = 9.52, composite ≤ 99.52.
