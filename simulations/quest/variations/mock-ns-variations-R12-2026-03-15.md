Written to `simulations/quest/golden/mock-ns-variate-R12-2026-03-15.md`.

---

## mock-ns -- Round 12 Variations

**Rubric**: v11 (C-01 through C-33, aspirational denominator 25).

**R11 gap being closed**: No single R11 variant achieved both C-32 (pre-computation position) and C-33 (5-column structured table). V-01 had the right position, wrong format. V-02 had the right format, wrong position. R11 V-04/V-05 (P-0 step) had position plus partial table format -- but "Resolves to" combined Step + Row type into one column, falling short of C-33's four separately-named columns.

**R12 central question**: Which form produces the most robust combined C-32 + C-33 adherence?

---

### Variation axes

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Lifecycle emphasis (top of S-3 + 5-column C-33 table, before computation cases) | Direct synthesis of R11 V-01 position + R11 V-02 table format. The C-33-compliant table (Token/Step/Row type/Paired token/Direction) sits at the very top of S-3, before Case 1. Tests whether the minimal synthesis achieves C-32+C-33 without step elevation. |
| **V-02** | Role sequence (P-0 as numbered step + 5-column C-33 table) | Same 5-column table as V-01 but promoted to P-0 before S-1. S-3 carries no embedded preamble. Tests whether step-level elevation produces stronger C-32/C-33 adherence than top-of-S-3 at equivalent table format. |
| **V-03** | Phrasing register (P-0 + imperative lookup directive) | Extends V-02's P-0 with an active lookup obligation: "when any bracket token appears, look it up before processing the row." Tests whether an imperative produces fewer token resolution errors than passive table availability. |
| **V-04** | Inertia framing (P-0 + S-3 computation boundary reminder) | Same P-0 as V-02, but S-3 opens with a named protocol checkpoint: "If entering from a regenerated context, read P-0 before proceeding." Tests whether naming the inertia failure mode improves adherence for regenerated-context runs. |
| **V-05** | Full convergence: P-0 + imperative + completeness assertion (seeds v12) | Extends V-03 with: (a) activation declaration ("ACTIVE from P-0 through A-5") and (b) completeness assertion -- all tokens listed, none unlisted, stop and report if an unlisted token is encountered. Seeds **C-34** (protocol completeness assertion) and **C-35** (activation scope declaration). |

---

**Key structural differences across variants:**

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| P-0 step | no | yes | yes | yes | yes |
| Preamble position | top of S-3 | P-0 | P-0 | P-0 | P-0 |
| Table format | 5-col | 5-col | 5-col | 5-col | 5-col |
| Imperative lookup | no | no | yes | no | yes |
| S-3 boundary reminder | no | no | no | yes | no |
| Activation declaration | no | no | no | no | yes |
| Completeness assertion | no | no | no | no | yes |
| Seeds | -- | -- | C-34 (partial) | -- | C-34 + C-35 |
