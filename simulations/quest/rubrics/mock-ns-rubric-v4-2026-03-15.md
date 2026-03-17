**v4 written** to `simulations/quest/rubrics/quest-rubric-mock-ns-v4-2026-03-15.md`.

---

**What changed in v4:**

Two new aspirational criteria from Round 3 excellence signals:

- **C-16** — FLAG immutability prohibition is declared **run-scoped**, not only step-sequential. C-14 requires prohibition at both sites; C-16 requires the compute-site prohibition to cover "anywhere in this run" rather than "in any subsequent step." V-02's `"MUST NOT be recomputed anywhere in this run"` is the clean example. The gap closed: conditional branches or regeneration paths that bypass normal step order can still reach header assembly — step-sequential prohibition doesn't cover them, run-scoped prohibition does.

- **C-17** — FLAG prohibition at the consumption site is the **first stated rule** of the header assembly step. C-14 requires prohibition language to appear somewhere at the site; C-17 requires it appear before any other header-construction instruction. V-01's `"The first rule of this step is: copy FLAG from S-4 verbatim. Do not rederive it."` is the reference pattern. The gap closed: prohibition present but buried after formatting or field-listing instructions leaves a competing instruction that can displace it under execution pressure.

**Scoring update:** Aspirational denominator changes from 7 to 9 (`pass/9 * 10`). Round 3 retro-scores depend on whether V-01 through V-04 carry run-scoped language (C-16) and first-rule prioritization (C-17) — from the scorecard evidence, V-01 and V-02 both show strong candidates for C-17; V-02 is the clear C-16 reference. Variants that don't carry both new patterns will score ≈ 97.8 (8/9 aspirational) rather than 100.
