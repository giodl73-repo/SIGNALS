Written to `simulations/quest/rubrics/corps-pr-rubric-v13-2026-03-17.md`.

---

**Three new criteria added (C-42, C-43, C-44):**

| ID | Gap closed | Source |
|----|-----------|--------|
| C-42 | C-39 conditional pre-commitment gap | V-01 pass: both verdict branches (SATISFIED / UNSATISFIED) expressed as named conditional antecedents in the template, pre-committing the failure-path form before any run executes |
| C-43 | C-40 anti-pattern labeling gap | V-02 pass vs. V-03/V-04 fail: a noncompliance label is insufficient — the prohibition must name the closed path, both criterion IDs (C-38 satisfied, C-40 superseding), and an explicit "do not use" directive |
| C-44 | Structural declaration-enforcement alignment gap | V-04 analysis: C-41 declaration (correct assignment of C-40 to table-column level) and template enforcement (retaining the "or" path) are orthogonal — C-44 requires them to be consistent |

**Scoring update:** aspirational denominator 33 → 36; each criterion worth 10/36 ≈ 0.278 pts. Perfect run still 100.

**R15 target:** V-04 (best R14 at 32/33 against v12) scores 33/36 against v13 — passes C-42 (two-branch conditional syntax already present), fails C-43 (note lacks "do not use" directive) and C-44 (C-41 declares C-40 at table-column level but "or" path not removed from template).
