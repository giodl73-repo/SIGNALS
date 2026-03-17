Written to `simulations/quest/rubrics/flow-throttle-rubric-v15-2026-03-16.md`.

**Three new criteria extracted from Round 14:**

| ID | Source | Pattern |
|----|--------|---------|
| **C-38** | V-02 (table form) | Annotation inventory declares entry count at header — completeness becomes a count-scan check, not a content-inspection check. Parallel to C-34 (closed observable set). |
| **C-39** | V-01, V-02, V-03 (all three) | Annotation inventory carries an explicit closure declaration: "This inventory is closed. An annotation not listed here does not exist as a contract requirement." Parallel to C-27 (closed-register declaration). |
| **C-40** | V-03 (SHALL/PROHIBITED form) | Annotation inventory includes a PROHIBITED clause for dropout with an inline annotation naming the failure mode it prevents. Extends C-16/C-18 prohibition-plus-annotation pattern into the annotation inventory itself. |

**Score delta**: 145 pts (29 × 5) → 160 pts (32 × 5), max composite 235 → 250. Golden threshold unchanged.

The structural progression in the FORMAT CONTRACT is now complete across three dimensions:

| Instructional layer | Contract-lock layer | Count-closed layer | Closure-declared layer | Prohibition-enforced layer |
|---------------------|---------------------|--------------------|------------------------|----------------------------|
| C-33 field-count declared | C-35 field-count contract-locked | — | — | — |
| C-34 observable-count at path labels | C-36 observable-count as role-activation condition | — | — | — |
| C-18 annotation required at anchor | C-37 annotation inventory contract-locked | **C-38** count declared | **C-39** inventory closed | **C-40** dropout PROHIBITED + annotation |
