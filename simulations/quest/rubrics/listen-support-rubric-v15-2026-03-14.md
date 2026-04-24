**v15 written** to `simulations/quest/rubrics/listen-support-rubric-v15-2026-03-15.md`.

---

**What changed v14 -> v15:**

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-44 | No-Exception Path Triple-Clause | C-43 | V-01, V-04, V-05 |
| C-45 | Phase Distribution Pre-Commitment | C-38 | V-02, V-04, V-05 |
| C-46 | Switching-Friction Minimum Count Gate | C-29 | V-03, V-05 |

**Aspirational: 175 -> 190 pts. Total ceiling: 265 -> 280.**

---

**R15 scores under v15 (280 ceiling):**

| Variation | Score | Fails |
|-----------|-------|-------|
| V-05 | 280/280 | -- |
| V-04 | 275/280 | C-46 FAIL |
| V-01 | 265/280 | C-42 FAIL, C-45 FAIL, C-46 FAIL |
| V-02 | 265/280 | C-43 FAIL, C-44 FAIL, C-46 FAIL |
| V-03 | 255/280 | C-39 FAIL, C-41 FAIL, C-42 FAIL, C-44 FAIL, C-45 FAIL |

**Signal logic summary:**

- **C-44**: C-43 applies triple-clause only to the EXCEPTION SIGN-OFF BLOCK Paraphrase field. The no-exception confirmation paths in Pass 2C (the common case) were left on a lower standard. V-01 upgraded both to match -- "do not paraphrase, do not summarize, copy it verbatim word-for-word" -- making the verbatim standard uniform across both paths.

- **C-45**: C-38 locks the inference rule and verbatim anchor before severity cells fill, but doesn't pre-commit how many tickets per phase. V-02 added a PHASE DISTRIBUTION block as a third required Step 4 item (gate upgrades to "all three items") with Step 4B constraint 0 verifying count compliance before body generation.

- **C-46**: C-29 requires a dedicated switching-friction sub-section with per-entry competitor fields, but the floor is one entry. V-03 raised the minimum to two, added a `SWITCHING-FRICTION COUNT: [N]` pre-declaration before entries, and added Pass 2B item 4 to verify count compliance. Single-entry sub-sections are now structural violations; undercounting is detectable without reading entries.
