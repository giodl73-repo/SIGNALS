**Written** to `simulations/quest/golden/corps-build-variate-R2-2026-03-17.md`

---

## Round 2 Summary

**3 new single-axis variations** (axes not covered in R1):

| Variation | Axis | Hypothesis | Strongest on |
|-----------|------|------------|--------------|
| **V-01** | Scaffold-first | Write org-chart.md skeleton before any role files; the skeleton is the structural contract | C-02, C-04, C-10 |
| **V-02** | Coverage audit loop | After all files written, explicit 4-check audit before org-chart is started; failures surfaced before they propagate | C-01, C-03, C-04, C-05 |
| **V-03** | Schema-as-contract | Define F-1..F-5 once at top, reference by ID throughout; single authoritative source reduces field omission | C-05, C-07 |

**2 combinations:**

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| **V-04** | Scaffold + Audit | Scaffold is the contract; audit enforces it — mutually reinforcing; closes both ends of the structural loop | C-04, C-10 |
| **V-05** | Schema + Scaffold + Audit + Resistance Profile | All four axes address distinct failure modes (field gaps, structural drift, IA boilerplate, missing files) — most defensible composite; tests whether accumulated structure is beneficial or creates prompt-length failure modes | All criteria |

**What changed from R1:** R1 was about *sequencing and phrasing*. R2 is about *verification mechanisms* — the scaffold is a pre-commitment, the audit is a post-check, and the schema contract is a stable reference object. V-05 is the candidate most likely to reach the golden threshold.
