Written to `simulations/quest/golden/topic-roadmap-variate-R17-2026-03-17.md`.

---

## Round 17 — V-01 through V-05

| Var | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | Score |
|-----|:----:|:----:|:----:|:----:|:----:|:----:|:-----:|
| V-01 | FULL | FULL | FULL | **FULL** | FAIL | FAIL | 64/68 = **9.41** |
| V-02 | FULL | FULL | FULL | partial | **FULL** | FAIL | 65/68 = **9.56** |
| V-03 | FULL | FULL | FULL | **FULL** | FAIL | **FULL** | 66/68 = **9.71** |
| V-04 | FULL | FULL | FULL | **FULL** | **FULL** | **FULL** | 68/68 = **10.00** |
| V-05 | FULL | FULL | FULL | **FULL** | **FULL** | **FULL** | 68/68 = **10.00** |

**Axes tested:**

- **V-01 (C-40 single-axis):** CONTRACT B adds formal `STRUCTURAL` / `VALUE` labeled categories with independent detection rules. §9 compliance obligation stays generic ("non-null... entry"). No self-sufficiency assertion.

- **V-02 (C-41 single-axis):** §9 compliance obligation names `'Bias blocked by guard'` exactly, with explicit "independently sufficient without consulting CONTRACT B" claim. CONTRACT B describes both failure modes in prose without formal category labels → C-40=partial(1).

- **V-03 (C-42 single-axis):** CONTRACT B gets taxonomy split (C-40=FULL as prerequisite) plus explicit `SCORER SELF-SUFFICIENCY DECLARATION` naming both test types with falsifiability clause. §9 stays generic → C-41=FAIL.

- **V-04 (combined, direct):** All three at FULL. Each criterion satisfied independently, no cross-reference language between guard and contract.

- **V-05 (combined, maximal):** All three at FULL plus explicit mutual reinforcement: §9 compliance obligation names the literal AND declares CONTRACT B as the governing document; C-42 clause names C-39/C-40 as structural consistency dependencies, making the self-sufficiency assertion machine-auditable as a consistency check.

**Key orthogonality note:** C-40 depends on C-39 FULL (need the value literal to define a VALUE violation). C-42 depends on both C-39 and C-40 FULL (self-sufficiency claim requires the literal and the taxonomy). V-03 therefore necessarily satisfies C-40 as a prerequisite — the single-axis isolation for C-42 holds, but C-40 comes along as a structural dependency, not as an intentional axis.
